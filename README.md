This is the content for the website at [hackasaurus.org][].

  [hackasaurus.org]: http://hackasaurus.org

## Prerequisites

You need Python version 2.6 or higher. All other dependencies are
self-contained within the project's code repository.

## Setup

Just run this at the terminal prompt:

    cd hackasaurus.org
    python manage.py runserver

Then, point your browser to http://localhost:8000/.

## Development

All static, unlocalized files are in the `static` directory, which are
placed at the root of the web site. The `templates` directory
contains localized [Jinja2][] templates that are located at `/<locale>/` on
the web site, where `<locale>` is the name of a locale like `en-US`.

  [Jinja2]: http://jinja.pocoo.org/

## Localization

The site uses GNU gettext for localization via [Babel][] and Jinja2's
[i18n extension][]. Soon we'll get the site listed on
[localize.mozilla.org][] so that anyone can easily help localize
the website.

  [Babel]: http://babel.edgewall.org/
  [i18n extension]: http://jinja.pocoo.org/docs/templates/#extensions
  [localize.mozilla.org]: https://localize.mozilla.org

## Deployment

Run this at the terminal prompt:

    python manage.py build
    
This will create a static version of the site, for all supported locales, in 
the `dist` directory. You can copy this directory to any web server that 
serves static files, such as Apache or Amazon S3.
