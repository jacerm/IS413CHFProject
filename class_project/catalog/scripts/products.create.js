$(function(){
   $("td").css("position", "relative");
   var product_type = $("#id_product_type").val();
   
   $("#id_status").closest("tr").toggle(product_type == "Rental_Product");
   $("#id_creator").closest("tr").toggle(product_type == "Individual_Product");
   $("#id_quantity").closest("tr").toggle(product_type == "Bulk_Product");
});

$("#id_product_type").on("change", function(){
    var product_type = $("#id_product_type").val();
    
   $("#id_status").closest("tr").toggle(product_type == "Rental_Product");
   $("#id_creator").closest("tr").toggle(product_type == "Individual_Product");
   $("#id_quantity").closest("tr").toggle(product_type == "Bulk_Product");
});

