from django.db import models

# Create your models here.

class Product(models.Model):
    # Tag Choices
    CHOICES = (
        ('ELECTR', 'Electronics'),
        ('CLOTH', 'Clothes'),
        ('SPORT', 'Sports'),
        ('PET', 'Pet supplies'),
        ('SOFTW', 'Software'),
        ('HEALTH', 'Health'),
    )

    name = models.CharField(null=False, blank=False, max_length=150)
    description = models.TextField(null=False, blank=False, max_length=1000)
    image = models.ImageField(null=False, blank=False, upload_to="images")
    tag = models.CharField(null=False, blank=False, choices=CHOICES, max_length=120)