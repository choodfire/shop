from django.db import models

# Create your models here.

class Store(models.Model):
    address = models.CharField(null=False, blank=False, max_length=300)
    mapImage = models.ImageField(null=False, blank=False, upload_to="shopMapImages")
    link = models.CharField(null=False, blank=False, max_length=1000)
    description = models.CharField(null=False, blank=False, max_length=500)
