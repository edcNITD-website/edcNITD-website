

const hamb = document.getElementById("hamb");
const navUL = document.getElementById("visible");
const hambicon = document.getElementById("subnav-icon");

hamb.addEventListener('click', () => {
    navUL.classList.toggle('show');
    hamb.classList.toggle('turn');
    hambicon.classList.toggle('change');
})

// //toggle active class
// $(document).ready(function () {
//     $(document).on("scroll", onScroll);

//     //smoothscroll
//     $('.subnav-item a[href^="#"]').on('click', function (e) {
//         e.preventDefault();
//         $(document).off("scroll");

//         $('.subnav-item a').each(function () {
//             $(this).removeClass('active');
//         })
//         $(this).addClass('active');

//         var target = this.hash,
//             menu = target;
//         $target = $(target);
//         $('html, body').stop().animate({
//             'scrollTop': $target.offset().top + 5
//         }, 500, 'swing', function () {
//             window.location.hash = target;
//             $(document).on("scroll", onScroll);
//         });
//     });
// });

$(document).ready(function () {
    $(document).on("scroll", onScroll);

    //smoothscroll
    $('.subnav-item a[href^="#"]').on('click', function (e) {
        e.preventDefault();
        $(document).off("scroll");

        $('.subnav-item a').each(function () {
            $(this).removeClass('active');
        })
        $(this).addClass('active');

        var target = this.hash,
            menu = target;
        $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top - 150
        }, 500);
    });
});

function onScroll(event) {
    var scrollPos = $(document).scrollTop();
    $('.subnav-item a').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (refElement.position().top <= (scrollPos + 90) && refElement.position().top + refElement.height() > scrollPos) {
            $('#subnav-link').removeClass("active");
            currLink.addClass("active");
        } else {
            currLink.removeClass("active");
        }
    });
}


