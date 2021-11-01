// navbar
$(".menu-toggle").click(function () {
  $(".nav").toggleClass("mobile-nav");
  $(this).toggleClass("is-active");
});

$(window).scroll(function () {
  $(".nav-wrapper").toggleClass("scrolled", $(this).scrollTop() > 90);
});

function closeMsg(element) {
  element.parentElement.parentElement.parentElement.style.display = 'none';
}