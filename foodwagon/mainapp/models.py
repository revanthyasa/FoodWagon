# Create your models here.
from django.db import models
from django.core import validators

class Users(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    repassword=models.CharField(max_length=20)
    def __str__(self):
        return self.username

class R(models.Model):
    name = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    rating = models.CharField(max_length=3)
    itemname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isveg = models.CharField(max_length=10)  
    itemimage = models.ImageField(upload_to='media/item_images/', default=None, null=True)

    def __str__(self):
        return self.name