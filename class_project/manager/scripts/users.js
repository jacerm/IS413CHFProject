$(function(){
   $("#users_tab").addClass("active");
   
});

$('.users_delete_link').click(function (){
    var href = $(this).attr("href");
    $("#users_confirm_delete_modal").attr("href", href)
    $(this).removeAttr("href");
    $('#users_delete_Modal').modal('show');  
});