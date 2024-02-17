from rest_framework import serializers

from models_app.models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ("category", )
