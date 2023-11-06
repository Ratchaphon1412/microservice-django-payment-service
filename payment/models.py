from django.db import models

import uuid
# Create your models here.

class User(models.Model):
    id = models.TextField(max_length=255,primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    customer_omise_id = models.CharField(max_length=255, blank=True, null=True)
    
class Statement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    amount = models.FloatField()
    pdf = models.TextField( blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    