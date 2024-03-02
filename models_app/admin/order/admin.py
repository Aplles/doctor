from django.contrib import admin

from models_app.admin.product_amount.admin import ProductAdminInline
from models_app.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'phone',
        'address',
        'delivery',
        'created_at',
    )
    list_display_links = (
        'id',
        'first_name',
        'phone',
    )
    inlines = (ProductAdminInline, )
