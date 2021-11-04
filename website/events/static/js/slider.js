const swiper = new Swiper('.swiper-container', {
  effect: 'coverflow',
  centeredSlides: true,
  slidesPerView: "auto",
  loop: true,
  speed: 600,
  
  autoplay: {
  delay: 3000,
    disableOnInteraction: false,
  },
  
  coverflowEffect: {
  rotate: 0,
  stretch: 0,
  depth: 100,
  modifier: 2,
  slideShadows: true,
  },
  
  pagination: {
  el: '.swiper-pagination',
  clickable: true,
  },
  
  navigation: {
  nextEl: '.swiper-button-next',
  prevEl: '.swiper-button-prev',
  },
  });