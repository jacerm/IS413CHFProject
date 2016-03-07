$(function(){
   $("#venues_tab").addClass("active");
});

$('.venues_delete_link').click(function (){
       var href = $(this).attr('href');
       $('#venues_confirm_delete_modal').attr('href', href);
       $(this).removeAttr('href');
       $('#venues_delete_modal').modal('show');  
});