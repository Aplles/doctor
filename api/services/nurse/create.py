from service_objects.fields import DictField
from service_objects.services import ServiceWithResult

from models_app.models import City


class NurseCreateService(ServiceWithResult):
    validated_data = DictField()

    def process(self):
        city = self._city
        return self

    def _nurse(self):
        pass

    @property
    def _city(self):
        _, city = City.objects.get_or_create(
            name=self.cleaned_data["validated_data"]["city"]
        )
        return city

    def _send_mail_promo_code(self):
        pass

    def _create_personal_promo_code(self):
        pass
