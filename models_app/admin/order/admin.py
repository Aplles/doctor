from django.contrib import admin
from django.db.models import Sum, F

from models_app.admin.product_amount.admin import ProductAdminInline
from models_app.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'phone',
        'address',
        # 'total_price',
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
        'created_at',
        'updated_at',
        # 'total_price',
    )
    fields = (
        'id',
        'first_name',
        'phone',
        'address',
        'description',
        'direction_image',
        'delivery',
        'created_at',
        'updated_at',
        'total_price',
    )

    # def total_price(self, obj):
    #     return obj.products.annotate(
    #         product_total_price=F('prices_product__price') * F('product_amounts__amount')
    #     ).aggregate(total=Sum('product_total_price'))['total']
    #
    # total_price.short_description = 'Общая стоимость услуг'
