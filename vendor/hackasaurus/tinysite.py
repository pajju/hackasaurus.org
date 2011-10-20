import os
import re
import mimetypes
import traceback
import shutil
import gettext
import jinja2
from wsgiref.simple_server import make_server
from wsgiref.util import FileWrapper, shift_path_info

locale_path_re = re.compile(r'^/([a-z][a-z])/.*')
mimetypes.add_type('application/x-font-woff', '.woff')

# Don't require localization files to exist for this locale.
NULL_LOCALE = 'en'

def simple_response(start, contents, code='200 OK', mimetype='text/plain'):
    start(code, [('Content-Type', mimetype),
                 ('Content-Length', str(len(contents)))])
    return [contents]

def handle_request(env, start, handlers):
    try:
        for handler in handlers:
            response = handler(env, start)
            if response is not None:
                return response
        return simple_response(start, "Not Found: %s" % env['PATH_INFO'],
                               code='404 Not Found')
    except Exception:
        msg = "500 INTERNAL SERVER ERROR\n\n%s" % traceback.format_exc()
        return simple_response(start, msg, code='500 Internal Server Error')

class BasicFileServer(object):
    def __init__(self, static_files_dir):
        self.ext_handlers = {}
        self.default_filenames = ['index.html']
        self.static_files_dir = static_files_dir

    def try_loading(self, filename, env, start):
        static_files_dir = self.static_files_dir
        fileparts = filename[1:].split('/')
        fullpath = os.path.join(static_files_dir, *fileparts)
        fullpath = os.path.normpath(fullpath)
        if (fullpath.startswith(static_files_dir) and
            not fullpath.startswith('.')):
            if os.path.isfile(fullpath):
                ext = os.path.splitext(fullpath)[1]
                handler = self.ext_handlers.get(ext)
                if handler:
                    mimetype, contents = handler(env, static_files_dir, fullpath)
                    return simple_response(start, contents, mimetype=mimetype)
                (mimetype, encoding) = mimetypes.guess_type(fullpath)
                if mimetype:
                    filesize = os.stat(fullpath).st_size
                    start('200 OK', [('Content-Type', mimetype),
                                     ('Content-Length', str(filesize))])
                    return FileWrapper(open(fullpath, 'rb'))
            elif os.path.isdir(fullpath) and not filename.endswith('/'):
                start('302 Found', [('Location', filename + '/')])
                return []
        return None

    def handle_request(self, env, start):
        filename = env['PATH_INFO']

        if filename.endswith('/'):
            for index in self.default_filenames:
                result = self.try_loading(filename + index, env, start)
                if result is not None:
                    return result
        return self.try_loading(filename, env, start)

class LocalizedTemplateServer(object):
    def __init__(self, template_dir, locale_dir, locale_domain):
        self.locale_dir = locale_dir
        self.locale_domain = locale_domain
        self.file_server = BasicFileServer(template_dir)
        self.file_server.ext_handlers.update({
            '.html': self.handle_file_as_jinja2_template
        })

    def handle_request(self, env, start):
        match = locale_path_re.match(env['PATH_INFO'])
        if match:
            locale = match.group(1)
            env = dict(env)
            env['locale_prefix'] = locale
            shift_path_info(env)
            if gettext.find(self.locale_domain, self.locale_dir, [locale]):
                env['translation'] = gettext.translation(self.locale_domain,
                                                         self.locale_dir,
                                                         [locale])
                                                         
            if 'translation' in env or locale == NULL_LOCALE:
                return self.file_server.handle_request(env, start)

    def handle_file_as_jinja2_template(self, wsgi_env, root_dir, fullpath):
        loader = jinja2.FileSystemLoader(root_dir, encoding='utf-8')
        env = jinja2.Environment(loader=loader, extensions=['jinja2.ext.i18n'])
        if 'translation' in wsgi_env:
            env.install_gettext_translations(wsgi_env['translation'])
        else:
            env.install_null_translations(newstyle=True)
        template = env.get_template(fullpath[len(root_dir):])
        return ('text/html', template.render().encode('utf-8'))

def run_server(port, static_files_dir, templates_dir,
               locale_dir, locale_domain):
    template_server = LocalizedTemplateServer(templates_dir, locale_dir,
                                              locale_domain)
    file_server = BasicFileServer(static_files_dir)
    handlers = [template_server.handle_request, file_server.handle_request]

    def application(env, start):
        return handle_request(env, start, handlers=handlers)

    httpd = make_server('', port, application)

    url = "http://127.0.0.1:%s/" % port
    print "development server started at %s" % url
    print "press CTRL-C to stop it"

    httpd.serve_forever()

def export_site(build_dir, static_files_dir, ext_handlers, ignore=None):
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    shutil.copytree(static_files_dir, build_dir, ignore=ignore)
    for dirpath, dirnames, filenames in os.walk(build_dir):
        files = [os.path.join(dirpath, filename)[len(build_dir)+1:]
                 for filename in filenames
                 if os.path.splitext(filename)[1] in ext_handlers]
        for relpath in files:
            print "processing special file: %s" % relpath
            abspath = os.path.join(static_files_dir, relpath)
            handler = ext_handlers[os.path.splitext(relpath)[1]]
            mimetype, contents = handler(static_files_dir, abspath)
            open(os.path.join(build_dir, relpath), 'w').write(contents)
    print "done.\n\nyour new static site is located at:\n%s" % build_dir
