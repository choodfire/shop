from django.contrib import admin
from .models import Product, Store

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')

admin.site.register(Product, ProductAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('address',)

admin.site.register(Store, StoreAdmin)