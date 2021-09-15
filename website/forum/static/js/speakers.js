//Init the carousel
initSlider();

function initSlider() {
  $(".speakers-carousel").owlCarousel({
    items: 1,
    loop: true,
    autoplay: true,
    onInitialized: startProgressBar,
    onTranslate: resetProgressBar,
    onTranslated: startProgressBar,
  });
}

function startProgressBar() {
  // apply keyframe animation
  if($(".speakers-carousel").autoplay==false){
    $("#bar").css({
      width: 0,
    });
  }else{
    $("#bar").css({
      width: "80%",
      transition: "width 5000ms"
    });
  }
}

function resetProgressBar() {
  $("#bar").css({
    width: 0,
    transition: "width 0s"
  });
}

