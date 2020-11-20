$(document).ready(function() {
    "use strict";

    $('.panel__responsive').slick({
        autoplay: true,
autoplaySpeed: 2000,
dots: false,
infinite: true,
speed: 300,
slidesToShow: 4,
slidesToScroll: 4,
// arrows: true,
prevArrow: $('#pannelPrev'),
nextArrow: $('#pannelNext'),
responsive: [
  {
    breakpoint: 1024,
    settings: {
      slidesToShow: 3,
      slidesToScroll: 3,
      infinite: true,
      dots: true
    }
  },
  {
    breakpoint: 754,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 2
    }
  },
  {
    breakpoint: 480,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1
    }
  }
]
});





  });


