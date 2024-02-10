from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Nurse


class NursePromoCodePresenceService(ServiceWithResult):
    promo_code = forms.CharField()

    def process(self):
        self.result = self._nurse
        return self

    @property
    def _nurse(self):
        try:
            return Nurse.objects.get(promo_code=self.cleaned_data["promo_code"])
        except Nurse.DoesNotExist:
            return None
