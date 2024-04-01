from django.contrib import admin

from models_app.models import ProductAmount, ProductPrice


class ProductAdminInline(admin.TabularInline):
    model = ProductAmount
    extra = 0
    readonly_fields = ['product_price']

    def product_price(self, obj):
        return ProductPrice.objects.get(
            product=obj.product,
            city__localization=obj.order.localization
        ).price

    product_price.short_description = 'Цена'
