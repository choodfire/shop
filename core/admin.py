from django.contrib import admin
from .models import Product, Store, CustomUser


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')


admin.site.register(Product, ProductAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('address',)


admin.site.register(Store, StoreAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
