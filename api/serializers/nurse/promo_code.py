from rest_framework import serializers

from models_app.models import Nurse


class NursePromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ("id", "first_name", "promo_code",)
