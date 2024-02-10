from rest_framework import serializers
from service_objects.services import ServiceOutcome

from api.services.nurse.create import NurseCreateService
from models_app.models import Nurse


class NurseCreateSerializer(serializers.ModelSerializer):
    city = serializers.CharField(write_only=True)
    promocode = serializers.CharField(write_only=True, required=False)
    affiliate_program = serializers.BooleanField(default=False, required=False)

    class Meta:
        model = Nurse
        fields = (
            "first_name",
            "phone",
            "email",
            "promocode",
            "certificate",
            "photo_with_passport",
            "city",
            "affiliate_program",
        )

    def create(self, validated_data):
        return ServiceOutcome(NurseCreateService, {
            "validated_data": validated_data
        }).result
