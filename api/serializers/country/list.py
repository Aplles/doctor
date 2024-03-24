from rest_framework import serializers

from api.serializers.city.list import CitySerializer
from models_app.models import City
from models_app.models import Country


class CountryListSerializer(serializers.ModelSerializer):
    currency = serializers.SerializerMethodField()
    cities = serializers.SerializerMethodField()
    default_city = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = (
            "id",
            "name",
            "currency",
            "localization",
            "cities",
            "default_city",
        )

    def get_cities(self, country):
        request = self.context['request']
        return CitySerializer(
            City.objects.filter(
                name__icontains=request.query_params.get('search', ''),
                country=country,
                is_approved=True
            ),
            many=True,
            read_only=True
        ).data

    def get_default_city(self, country):
        if country.default_city and country.default_city.is_approved:
            return CitySerializer(country.default_city).data

    def get_currency(self, country):
        return country.currency.value
