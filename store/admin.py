from django.contrib import admin
from .models import Store
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ('address',)


admin.site.register(Store, StoreAdmin)
