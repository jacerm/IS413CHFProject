from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel

# Define models here

class Product(PolymorphicModel):
    name = models.TextField(null=True, blank=True)
    wholesale_cost = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    add_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    image = models.TextField(null=True, blank=True)
    
admin.site.register(Product)

STATUS_CHOICES = (
    ("Available", "Available"),
    ("Unavailable", "Unavailable"),
)
STATUS_CHOICES_MAP = dict(STATUS_CHOICES)

class RentalProduct(Product):
    class_name = "Rental Product"
    status = models.TextField(null=True, blank=True, choices=STATUS_CHOICES)
    
admin.site.register(RentalProduct)
    
class IndividualProduct(Product):
    class_name = "Individual Product"
    creator = models.ForeignKey('account.User')
    
admin.site.register(IndividualProduct)
    
class BulkProduct(Product):
    class_name = "Bulk Product"
    quantity = models.IntegerField(default=0)

admin.site.register(BulkProduct)

