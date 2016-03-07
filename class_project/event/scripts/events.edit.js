$(function(){
   $("td").css("position", "relative");
});

$('.areas_delete_link').click(function (){
       var href = $(this).attr('href');
       $('#areas_confirm_delete_modal').attr('href', href);
       $(this).removeAttr('href');
       $('#areas_delete_modal').modal('show');  
});