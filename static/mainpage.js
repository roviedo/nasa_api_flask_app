var grid = document.querySelector('.grid');
var msnry = new Masonry( grid, {
  // options...
  itemSelector: '.grid-item',
  columnWidth: '.grid-sizer',
  gutter: 10,
  horizontalOrder: true,
  percentPosition: true
});

imagesLoaded( document.querySelector('.grid'), function( instance ) {
  console.log('all images are loaded');
  msnry.layout();
});

var submitButton = document.querySelector('input[type="submit"]');
submitButton.addEventListener('click', function () {
    var solElem = document.querySelector('input[type="number"]');
    var cameraElem = document.getElementById('camera');
    var solElemValue = 1000;
    if (parseInt(solElem.value) < 1000) solElemValue = parseInt(solElem.value);
    window.location.href = window.location.pathname + '?camera=' + cameraElem.value + '&sol=' + solElemValue;
});