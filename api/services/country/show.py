from functools import lru_cache
from django import forms
from service_objects.services import ServiceWithResult
from rest_framework.exceptions import NotFound

from models_app.models import Country


class CountryShowService(ServiceWithResult):
    localization = forms.CharField()

    custom_validations = ['country_presence']

    def process(self):
        self.run_custom_validations()
        self.result = self._country
        return self

    @property
    @lru_cache
    def _country(self):
        try:
            return Country.objects.get(localization=self.cleaned_data['localization'])
        except Country.DoesNotExist:
            return None

    def country_presence(self):
        if not self._country:
            raise NotFound("Country with this locale not found")
