var a = screen.width;

var n=3
console.log(a)

if (a<700){
    var n=1;
}
else if (a>=700 && a<=1200){
  var n=3;
}

console.log(n)


$(document).on('ready', function() {
    $(".regular").slick({
      dots: true,
      infinite: true,
      slidesToShow: n,
      centerMode:true,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1000,
    });
});