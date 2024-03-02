from django.contrib import admin

from models_app.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_approved'
    )
