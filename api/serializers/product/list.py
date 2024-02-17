from rest_framework import serializers

from api.serializers.category.show import CategorySerializer
from models_app.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
