$(function(){
   $("#products_tab").addClass("active");
});

$('.products_delete_link').click(function (){
    var href = $(this).attr('href');
    $('#products_confirm_delete_modal').attr('href', href);
    $(this).removeAttr('href');
    $('#products_delete_modal').modal('show');  
});

$('.quantity_btn').click(function(e) {
    e.preventDefault();
    var href = $(this).attr("href");//getting id
    $(this).siblings('#quantity_val').load(href);
});