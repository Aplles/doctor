from rest_framework import serializers

from api.serializers.category.show import CategoryShowSerializer
from models_app.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryShowSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
