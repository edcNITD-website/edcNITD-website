//about
function toggleSubAbout(element) {
  console.log(element);
  id = element.id;
  let content_element = document.getElementById(id + "-content");
  let heading_element = document.getElementById(id + "-heading");
  let sub_about_element = document.getElementById(id + "-sub_about");
  if (element.innerHTML == "+") {
    element.innerHTML = "-";
  } else {
    element.innerHTML = "+";
  }
  content_element.classList.toggle("active");
  heading_element.classList.toggle("active");
  sub_about_element.classList.toggle("active");
}


// faq
function toggleAnswer(element) {
  let id = element.id.split('-')[0];
  console.log(element.id);
  let answer_element = document.getElementById(id + "-answer");
  let question_element = document.getElementById(id + "-question");
  let faq_element = document.getElementById(id + "-faq");
  if (element.innerHTML == "+") {
    element.innerHTML = "-";
  } else {
    element.innerHTML = "+";
  }
  answer_element.classList.toggle("active");
  question_element.classList.toggle("active");
  faq_element.classList.toggle("active");
}

// carousel
const slides = document.querySelectorAll(".slide");
const next = document.querySelector("#next");
const prev = document.querySelector("#prev");
const auto = true; // Auto scroll
const intervalTime = 6000;
let slideInterval;

const nextSlide = () => {
  const current = document.querySelector(".current");
  current.classList.remove("current");
  if (
    current.nextElementSibling == slides[1] ||
    current.nextElementSibling == slides[2]
  ) {
    current.nextElementSibling.classList.add("current");
  } else {
    slides[0].classList.add("current");
  }
  setTimeout(() => current.classList.remove("current"));
};

const prevSlide = () => {
  const current = document.querySelector(".current");
  current.classList.remove("current");
  if (current.previousElementSibling) {
    current.previousElementSibling.classList.add("current");
  } else {
    slides[slides.length - 1].classList.add("current");
  }
  setTimeout(() => current.classList.remove("current"));
};

// Button events
next.addEventListener("click", (e) => {
  nextSlide();
  if (auto) {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, intervalTime);
  }
});

prev.addEventListener("click", (e) => {
  prevSlide();
  if (auto) {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, intervalTime);
  }
});

// Auto slide
if (auto) {
  slideInterval = setInterval(nextSlide, intervalTime);
}

(function ($) {
  "use strict";
  $(document).ready(function () {
    // Testimonials carousel (uses the Owl Carousel library)
    $(".internships-carousel").owlCarousel({
      autoplay: true,
      dots: true,
      loop: true,
      items: 1
    });
  });
})(jQuery);