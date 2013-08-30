$(document).ready(function() {
    mobileNavExpandCollapse();
    $(window).scroll(roll_on_scroll);

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

    function roll_on_scroll(){
        var scroll = document.documentElement.scrollTop;
        var intro_bottom = $('#blue-avatar').position().top;
        if(scroll >= intro_bottom){
            $('.intro-avatar').attr('class', 'intro-avatar rollout');

        } else if(scroll < intro_bottom && $('.rollout').length){
            console.log('rollin');
            $('.intro-avatar').attr('class', 'intro-avatar rollin');
        }
    }
});