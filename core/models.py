from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.

CATEGORIES = [
        ('ELECTR', 'Electronics'),
        ('CLOTH', 'Clothes'),
        ('SPORT', 'Sports'),
        ('PET', 'Pet supplies'),
        ('SOFTW', 'Software'),
        ('HEALTH', 'Health'),
    ]

class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150, default="No name")
    short_description = models.TextField(null=False, blank=False, max_length=100, default="No short description")  # for product card in catalog
    long_description = models.TextField(null=False, blank=False, max_length=1000, default="No description")  # for product in its card
    price = models.IntegerField(null=False, blank=False, default=0)
    image = models.ImageField(null=False, blank=False, upload_to="images")
    category = models.CharField(null=False, blank=False, choices=CATEGORIES, max_length=120)  # category

    class Meta:
        ordering = ['-id']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class Store(models.Model):
    address = models.CharField(null=False, blank=False, max_length=300)
    mapImage = models.ImageField(null=False, blank=False, upload_to="shopMapImages")
    link = models.CharField(null=False, blank=False, max_length=1000)
    description = models.CharField(null=False, blank=False, max_length=500)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default.jpg', blank=True, null=True)

    def get_absolute_url(self):
        # from django.urls import reverse
        return reverse('core:profile')

    # def __str__(self):
    #     return self.
