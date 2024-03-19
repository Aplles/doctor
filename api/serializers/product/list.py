from rest_framework import serializers

from models_app.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField()
    discount_price = serializers.IntegerField()

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "image",
            "price",
            "discount_price",
        )
