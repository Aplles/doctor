from django.contrib import admin

from models_app.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'discount_price',
    )
    list_display_links = (
        'id',
        'title',
    )
    ordering = ('id', 'title',)
