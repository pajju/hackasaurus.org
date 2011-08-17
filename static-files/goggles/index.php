<?php include_once("../include/module/head.php")?>

<?php include_once("../include/module/header.php")?>
	
<section class="inner-page tool-goggles" role="main">

	<div class="content-primary">
	
		<div class="browser-warning">
			<h2>Euston, we have a problem.</h2>
			
			<p>It looks like you're using Internet Explorer.</p>
			
			<p>Before you use the Goggles, you'll need to upgrade to a newer browser.</p>
			
			<p>The Goggles rely on some smart new features that are only in browsers like Opera, Safari, Chrome and Firefox.</p>
			
			<a class="firefox-plug" href='http://www.mozilla.org/firefox?WT.mc_id=aff_en12&WT.mc_ev=click'><img src='http://www.mozilla.org/contribute/buttons/120x240bubble_g.png' alt='Firefox Download Button' border='0' /></a>
			
		</div>
		
		<h1>X-Ray Goggles</h1>
		
		<h2>Step 1) Install X-Ray Goggles</h2>
		<p>Drag the X-Ray Goggles up to your web browser's bookmarks toolbar:</p>
		
		<p><a id="bookmarklet-link" href="javascript:(function(){'use strict';var script=document.createElement('script');script.src='https://secure.toolness.com/webxray/webxray.js';script.className='webxray';document.head.appendChild(script);})();">Web X-Ray Goggles</a></p>
		
		<img class="screenshot bookmarklet-demo" src="http://hackasaurus.org/include/image/bookmarklet.gif" alt="bookmarklet" width="328" height="142" />
	
	<div class="helper">
	<h3>Having trouble?</h3>
    <p>Make sure your browser's bookmarks toolbar is turned on. (<a href="http://support.mozilla.com/en-US/kb/how-do-i-use-bookmarks#w_how-do-i-turn-on-the-bookmarks-toolbar">How?</a>)</p>
	</div>
		
		<h2>Step 2: Turn them on</h2>
		<p>Click on the X-Ray Goggles to activate. (Warning: may alter reality.)</p>

<img class="screenshot" src="http://hackasaurus.org/include/image/screenshot-bookmarklet.png" alt="Example of the bookmarklet installed" />
		
		<h2>Step 3: Bust your hack</h2>
		<p>Go to your favorite web page. Mouse over any element. Hit "R" to remix it.</p>


	<!-- Examples Slideshow -->
	<div class="examples">
		<div class="slideshow-gallery">
			<div class="slideshow">
				<div class="slides">
					<ul>
						<li><img src="http://hackasaurus.org/include/image/slides/8.jpg" alt="" /></li>
						<li><img src="http://hackasaurus.org/include/image/slides/7.jpg" alt="" /></li>
						<li><img src="http://hackasaurus.org/include/image/slides/1.jpg" alt="" /></li>
						<li><img src="http://hackasaurus.org/include/image/slides/6.jpg" alt="" /></li>
					</ul>
					<div class="loader">
						<img src="http://hackasaurus.org/include/image/loader.gif" alt="loader"/>
					</div>
				</div>
				<p id="next">Next</p>
				<p id="prev">Prev</p>
			</div>
		</div>
	</div>
	<!-- End Examples Slideshow -->

	
	</div>
	
	<div class="content-secondary goggle-controls">
	
		<img src="http://hackasaurus.org/include/image/supergirl.png" alt="supergirl" width="300" height="330" />
		
		<h2>X-Ray Goggles controls:</h2>
		
		<h3>Remix</h3>
		<kbd>R</kbd>
		<p>Remix an element using HTML.</p>
		
		<h3>Inspect</h3>
		<kbd>I</kbd>
		<p>Learn more about the element</p>
		
		<h3>Tear</h3>
		<kbd>T</kbd>
		<p>Copy and paste the code to remix on your own page.</p>
		
		<h3>Off</h3>				
		<kbd>Esc</kbd>	
		<p>Hit "Esc" to deactivate.</p>
		
	</div>
	
</section>

<script type="text/javascript" src="http://hackasaurus.org/include/script/jquery.cycle.all.min.js"></script>
<script type="text/javascript">
$(document).ready(function() {
    $('.slides ul').cycle({
		fx: 'fade',
		startingSlide: 2,
		pause: 0,
		prev: '#prev',
		speed: 500,
		next: '#next'
	});
});
</script>

<?php include_once("../include/module/footer.php")?>