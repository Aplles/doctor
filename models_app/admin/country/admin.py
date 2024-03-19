from django.contrib import admin

from models_app.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'localization',
        'currency',
        'default_city',
    )
