$(document).ready(function(){

    var yPosition;
    var scrolled = 0;
    
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.logo');
    
    $(window).scroll(function(){
    
    scrolled = $(window).scrollTop();
    
    for (var i = 0; i < $parallaxElements.length; i++){
    
    var yPosition = (scrolled * 0.10*(i + 1));
    
    $parallaxElements.eq(i).css({ top: yPosition + 'px' });
    
    }
    $logo.css({
        top: (scrolled * 0.30) + 'px'   
    });
    
});
});