from rest_framework import serializers

from models_app.models import City


class CityShowSerializer(serializers.ModelSerializer):
    currency = serializers.CharField(source='country.currency.value')

    class Meta:
        model = City
        fields = (
            "id",
            "name",
            "localization",
            "currency"
        )
