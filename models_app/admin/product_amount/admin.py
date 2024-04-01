from django.contrib import admin

from models_app.models import ProductAmount, ProductPrice


class ProductAdminInline(admin.TabularInline):
    model = ProductAmount
    extra = 0
    readonly_fields = ['product_price']

    def product_price(self, obj: ProductAmount):
        return ProductPrice.price_in_city(
            obj.product, obj.order.localization
        )

    product_price.short_description = 'Цена'
