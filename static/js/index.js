$(document).ready(function(){

//Owl carousel script
$('.deposit-cards-wrapper').owlCarousel({
  margin:20,
  loop:true,
  autoplay:true,
  autoplayTimeout:1500,
  autoplayHoverPause:true,
  responsive:{
  0:{
  items:1,
  nav:false
  },
  450:{
  items:2,
  nav:false
  },
  650:{
  items:3,
  nav:false
  }
  }
});
});