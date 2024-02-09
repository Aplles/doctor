from django.contrib import admin

from models_app.admin.product_amount.admin import ProductAdminInline
from models_app.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductAdminInline, )
