from functools import lru_cache
from django import forms
from service_objects.services import ServiceWithResult
from rest_framework.exceptions import NotFound

from models_app.models import City


class CityShowService(ServiceWithResult):
    localization = forms.CharField()

    custom_validations = ['city_presence']

    def process(self):
        self.run_custom_validations()
        self.result = self._city
        return self

    @property
    @lru_cache
    def _city(self):
        try:
            return City.objects.get(localization=self.cleaned_data['localization'])
        except City.DoesNotExist:
            return None

    def city_presence(self):
        if not self._city:
            raise NotFound("City with this locale not found")
