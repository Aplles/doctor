from django.contrib import admin

from models_app.models import ProductPrice


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'price',
        'discount_price',
        'product',
        'city',
    )
