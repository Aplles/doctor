from rest_framework import serializers

from models_app.models import Product
from models_app.models import ProductAmount


class ProductAmountCreateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    amount = serializers.IntegerField(min_value=1)

    class Meta:
        model = ProductAmount
        fields = ("id", "amount")
