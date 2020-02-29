(function($) {
    function FooterBottom() { 
        $('body').css('margin-bottom', $('.footer').outerHeight())
    };

    FooterBottom();
    window.addEventListener('resize', FooterBottom, false);  
})(jQuery);

$(document).ready(function(){
    $('.dropdown').on('show.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown("fast");
    });

    $('.dropdown').on('hide.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp("fast");
    });
});

$(document).ready(function(){
    $(function () {
        'use strict'
        $('[data-toggle="offcanvas"]').on('click', function () {
            $('.offcanvas-collapse').toggleClass('open');
            $('.navbar-toggler-icon').toggleClass('open')
        })
    })
});

$(document).ready(function(){
    function handleFirstTab(e) {
        if (e.keyCode === 9) {
            document.body.classList.add('user-is-tabbing');

            window.removeEventListener('keydown', handleFirstTab);
            window.addEventListener('mousedown', handleMouseDownOnce);
        }
    }

    function handleMouseDownOnce() {
        document.body.classList.remove('user-is-tabbing');

        window.removeEventListener('mousedown', handleMouseDownOnce);
        window.addEventListener('keydown', handleFirstTab);
    }

    window.addEventListener('keydown', handleFirstTab);
});

$(document).ready(function(){
    $(window).scroll(function(){
        if ($(this).scrollTop() > 750) {
            $('.scroll-to-top').fadeIn(200);
        } 
        else {
            $('.scroll-to-top').fadeOut(200);
        }
    });
    $('.scroll-to-top').click(function(){
        $('html, body').animate({scrollTop : 0},300);
        return false;
    });
});

$(document).ready(function(){
    var $grid = $('.img-grid').masonry({
        itemSelector: 'figure',
        percentPosition: true
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress( function() {
        $grid.masonry();
    });  
});

(function() {
    'use strict';
    window.addEventListener('load', function() {
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

function numberWithCommas(number) {
    var parts = number.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return parts.join(".");
}
$(document).ready(function() {
    $(".number").each(function() {
        var num = $(this).text();
        var commaNum = numberWithCommas(num);
        $(this).text(commaNum);
    });
});

$(document).ready(function(){
    var products = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        prefetch: '../search-data.json'
    });

    $('.typeahead').typeahead(null, {
        name: 'search-data',
        source: products
    });
});

$(document).ready(function(){
    $('.search-input').on('focus', function() {
        $('.search-box').addClass('w-100');
    });

    $('.search-input').on('focusout', function() {
        $('.search-box').removeClass('w-100');
    });
});

(function($) {
    function MtchHeight() { 
        if(window.matchMedia('(min-width: 576px)').matches){
            $(function() {
                $('.subject-card-caption').matchHeight({
                    byRow: false
                });
            });
        }
        else {
            $(function() {
                $('.subject-card-caption').matchHeight({
                    byRow: true
                });
            });
        };

        $(function() {
            $('.subject-card').matchHeight({
                byRow: false
            });
        });
        
        $(function() {
            $('.product-item a').matchHeight({
                byRow: false
            });
        });
        
        $(function() {
            $('.news-item a').matchHeight({
                byRow: false
            });
        });
    };

    MtchHeight();
    window.addEventListener('resize', MtchHeight, false);  
})(jQuery);

(function($) {
    function NavbarScroll() {
        var scroll = $(window).scrollTop(),
            topbar = $('.topbar').outerHeight();

        if(scroll > topbar){
            $('.navbar').addClass('fixed-top');
            $('.topbar').css('margin-bottom','54px');
            $('.offcanvas-collapse').addClass('now-scrolling');
        } 
        else {
            $('.navbar').removeClass('fixed-top');
            $('.topbar').css('margin-bottom','0');
            $('.offcanvas-collapse').removeClass('now-scrolling');
        }
    };

    NavbarScroll();
    window.addEventListener('scroll', NavbarScroll, false);  
})(jQuery);