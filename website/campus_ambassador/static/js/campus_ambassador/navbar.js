function toggleMenu() {
    let menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
    menu.classList.toggle('flex');
}

$(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
        $('#navbar').addClass('bg-gradient-to-r');
        $('#navbar').addClass('from-blue-900');
        $('#navbar').addClass('to-fuchsia-900');
        
    } else {
        $('#navbar').removeClass('bg-gradient-to-r');
        $('#navbar').removeClass('from-blue-900');
        $('#navbar').removeClass('to-fuchsia-900');
    }
  });