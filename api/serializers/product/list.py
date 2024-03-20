from rest_framework import serializers

from models_app.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(default=0)
    discount_price = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "image",
            "price",
            "discount_price",
        )
