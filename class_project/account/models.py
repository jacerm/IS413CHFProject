from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Define models here
class User(AbstractUser):
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

admin.site.register(User)