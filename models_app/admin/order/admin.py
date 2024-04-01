from django.contrib import admin
from django.db.models import Sum, F

from models_app.admin.product_amount.admin import ProductAdminInline
from models_app.models import Order, ProductPrice


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'phone',
        'address',
        'total_price',
        'delivery',
        'created_at',
    )
    list_display_links = (
        'id',
        'first_name',
        'phone',
    )
    inlines = (ProductAdminInline, )
    readonly_fields = (
        'id',
        'localization',
        'created_at',
        'updated_at',
        'total_price',
    )
    fields = (
        'id',
        'first_name',
        'phone',
        'address',
        'description',
        'direction_image',
        'delivery',
        'localization',
        'created_at',
        'updated_at',
        'total_price',
    )

    def total_price(self, obj: Order):
        total_price = 0
        for product in obj.products.all():
            total_price += ProductPrice.price_in_city(
                product=product,
                city_localization=obj.localization
            ) * product.product_amounts.filter(order=obj).first().amount
        return total_price

    total_price.short_description = 'Общая стоимость услуг'
