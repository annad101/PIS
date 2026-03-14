$(document).ready(function(){

    $('.one-post').hover(
        function(event){

            console.log("Навели");
            console.log(event.currentTarget);

            $(event.currentTarget)
                .find('.one-post-shadow')
                .animate({opacity: '0.1'}, 300);

        },

        function(event){

            console.log("Вывели");

            $(event.currentTarget)
                .find('.one-post-shadow')
                .animate({opacity: '0'}, 300);

        }
    );

    $(document).ready(function(){

        $('.header img').hover(function(){
    
            $(this).animate({
                width: "+=20px"
            }, 300);
    
        }, function(){
    
            $(this).animate({
                width: "-=20px"
            }, 300);
    
        });
    
    });

});