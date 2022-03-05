function toggleMenu() {
    let menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
    menu.classList.toggle('flex');
}

$(window).scroll(function() {
    if ($(this).scrollTop() > 50) {
        $('#navbar').addClass('bg-black');
        $('.nav-item').addClass('scroll');
        
    } else {
        $('#navbar').removeClass('bg-black');
        $('.nav-item').removeClass('scroll');
    }
  });