from django.contrib import admin

from models_app.models import ProductAmount


@admin.register(ProductAmount)
class ProductAmountAdmin(admin.ModelAdmin):
    pass
