from django.contrib import admin
from APIApp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Product, ProductAdmin)

