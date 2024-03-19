from django.contrib import admin

from models_app.models import Product, ProductPrice


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title'
    )
    list_display_links = (
        'id',
        'title',
    )
    ordering = ('id', 'title',)
    inlines = (ProductPriceInline, )
