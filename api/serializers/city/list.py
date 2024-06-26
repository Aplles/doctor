from rest_framework import serializers

from models_app.models import City


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            "id",
            "name",
            "localization",
        )
