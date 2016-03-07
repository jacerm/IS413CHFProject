$(function(){
   $("#loginForm").ajaxForm({
       target: '#jquery-loadmodal-js-body',
       success: function() { 
            $('#htmlExampleTarget').fadeIn('slow'); 
        } 
   }); 
});