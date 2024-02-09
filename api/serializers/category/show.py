from rest_framework import serializers

from models_app.models import Category


class CategoryShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
