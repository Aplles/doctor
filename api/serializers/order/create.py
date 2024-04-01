from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from service_objects.services import ServiceOutcome

from api.serializers.product.create import ProductAmountCreateSerializer
from api.services.order.create import OrderCreateService
from models_app.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    products = ProductAmountCreateSerializer(many=True, write_only=True, required=False)
    direction_image = Base64ImageField(required=False)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "phone",
            "address",
            "description",
            "localization",
            "direction_image",
            "delivery",
            "created_at",
            "updated_at",
            "products"
        )

    def create(self, validated_data: dict):
        return ServiceOutcome(OrderCreateService, {
            "validated_data": validated_data
        }).result
