// navbar
var menu = document.querySelector('.menu-toggle');

function toggleMenu(element) {
  var nav = document.querySelector(".nav");
  nav.classList.toggle("mobile-nav");
  element.classList.toggle("is-active");
}

$(window).scroll(function () {
  $(".nav-wrapper").toggleClass("scrolled", $(this).scrollTop() > 90);
});

function closeMsg(element) {
  element.parentElement.parentElement.parentElement.style.display = 'none';
}