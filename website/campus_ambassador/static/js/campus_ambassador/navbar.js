function toggleMenu() {
    let menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
    menu.classList.toggle('flex');
}

$(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
        $('#navbar').addClass('bg-slate-900');
        $('.nav-item').addClass('scroll');
        
    } else {
        $('#navbar').removeClass('bg-slate-900');
        $('.nav-item').removeClass('scroll');
    }
  });