from django.contrib import admin

from models_app.models import ProductAmount


class ProductAdminInline(admin.TabularInline):
    model = ProductAmount
    extra = 0


@admin.register(ProductAmount)
class ProductAmountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'amount',
        'product',
        'order',
    )
