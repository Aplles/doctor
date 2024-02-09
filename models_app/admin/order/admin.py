from django.contrib import admin

from models_app.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
