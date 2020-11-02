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