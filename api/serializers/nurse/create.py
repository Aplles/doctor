from rest_framework import serializers
from service_objects.services import ServiceOutcome

from api.services.nurse.create import NurseCreateService
from models_app.models import Nurse


class NurseCreateSerializer(serializers.ModelSerializer):
    city = serializers.CharField(write_only=True)
    affiliate_program = serializers.BooleanField(default=False)

    class Meta:
        model = Nurse
        fields = "__all__"

    def create(self, validated_data):
        return ServiceOutcome(NurseCreateService, {
            "validated_data": validated_data
        }).result
