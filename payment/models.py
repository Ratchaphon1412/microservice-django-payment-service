from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=255,primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    customer_omise_id = models.CharField(max_length=255, blank=True, null=True)