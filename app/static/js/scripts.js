$(document).ready(function() {
    mobileNavExpandCollapse();
    showScrollTop();
    roll_on_scroll_init();
    $(window).scroll(function() {
        roll_on_scroll();
        showScrollTop();
    });
    $('a[href="#top"]').on('click', function(e) {
        e.preventDefault();
        scrollToAnchor($(this).attr('href'));
    })

    function mobileNavExpandCollapse(){
        $('#nav-control').on('click', function(){
            var $this = $('#navigation');
            if($this.hasClass('expanded')){
                $this.animate({height: "70px"}, 300, function(){
                    $(this).removeClass('expanded');
                });
            } else {
                $this.animate({height: "320px"}, 500, function(){
                    $(this).addClass('expanded');
                });
            }
        });
    }

    function roll_on_scroll_init(){
        //$('.intro-avatar').attr('class', 'intro-avatar rollin');
    };
    function roll_on_scroll(){
        var scroll = $(window).scrollTop(); //document.documentElement.scrollTop;
        var intro_bottom = $('#blue-avatar').position().top;
        if(scroll >= intro_bottom){
            $('.intro-avatar').attr('class', 'intro-avatar rollout');

        } else if(scroll < intro_bottom && $('.rollout').length){
            $('.intro-avatar').attr('class', 'intro-avatar rollin');
        }
    }

    function showScrollTop() {
        if($(window).scrollTop() >= 100) {
            $('#backToTop').css('opacity', 1);
        } else {
            $('#backToTop').css('opacity', 0);
        }
    }
    function scrollToAnchor(aID){
        var aTag = $(aID.substring(aID.indexOf("#")));
        $('html,body').animate({scrollTop: aTag.offset().top});
    }   
});