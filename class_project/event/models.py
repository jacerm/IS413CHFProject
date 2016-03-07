from django.db import models
from django.contrib import admin
from polymorphic.models import PolymorphicModel

# Define models here
class Venue(models.Model):
    name = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zip = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return '%s' % (self.name)
    
class Event(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    venue = models.ForeignKey('event.Venue')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return '%s' % (self.name)
    
class Area(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    place_number = models.TextField(null=True, blank=True)
    event = models.ForeignKey('event.Event')