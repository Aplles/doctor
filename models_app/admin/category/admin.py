from django.contrib import admin

from models_app.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
