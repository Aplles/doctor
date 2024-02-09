from django.contrib import admin

from models_app.models import Nurse


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    pass
