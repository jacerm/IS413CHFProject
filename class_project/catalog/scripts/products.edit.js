$(function(){
   $("td").css("position", "relative");
   var product_type = $("#product_class").text();
   
   $("#id_status").closest("tr").toggle(product_type == "Rental Product");
   $("#id_creator").closest("tr").toggle(product_type == "Individual Product");
   $("#id_quantity").closest("tr").toggle(product_type == "Bulk Product");
});

