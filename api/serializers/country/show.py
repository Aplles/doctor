from rest_framework import serializers

from api.serializers.city.list import CityListSerializer
from models_app.models import Country


class CountryShowSerializer(serializers.ModelSerializer):
    default_city = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = (
            "id",
            "name",
            "localization",
            "currency",
            "default_city"
        )

    def get_default_city(self, country):
        if country.default_city and country.default_city.is_approved:
            return CityListSerializer(country.default_city).data
