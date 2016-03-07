$(function(){
   $("#events_tab").addClass("active");
});

$('.events_delete_link').click(function (){
       var href = $(this).attr('href');
       $('#events_confirm_delete_modal').attr('href', href);
       $(this).removeAttr('href');
       $('#events_delete_modal').modal('show');  
});