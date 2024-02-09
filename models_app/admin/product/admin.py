from django.contrib import admin

from models_app.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
