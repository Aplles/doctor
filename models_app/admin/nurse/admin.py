from django.contrib import admin

from models_app.models import Nurse


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'phone',
        'email',
        'promo_code',
        'created_at',
        'city',
    )
