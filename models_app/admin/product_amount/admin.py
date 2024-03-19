from django.contrib import admin

from models_app.models import ProductAmount


class ProductAdminInline(admin.TabularInline):
    model = ProductAmount
    extra = 0
    readonly_fields = ['product_price']

    def product_price(self, obj):
        return obj.product.price

    product_price.short_description = 'Цена'
