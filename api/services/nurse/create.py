from django.utils.crypto import get_random_string
from service_objects.fields import DictField
from service_objects.services import ServiceWithResult

from models_app.models import City
from models_app.models import Nurse


class NurseCreateService(ServiceWithResult):
    validated_data = DictField()

    def process(self):
        affiliate_program, promo_code = self.validate()
        self.result = self._nurse

        if affiliate_program:
            self._create_personal_promo_code()

        if promo_code:
            self._send_mail_promo_code()

        return self

    def validate(self):
        affiliate_program = promo_code = None
        self._data['city'] = self._city
        if self._data["affiliate_program"]:
            affiliate_program = self._data.pop("affiliate_program")
        if self._data["promo_code"]:
            promo_code = self._data.pop("promo_code")
        return affiliate_program, promo_code

    @property
    def _data(self):
        return self.cleaned_data["validated_data"]

    @property
    def _nurse(self):
        return Nurse.objects.create(**self._data)

    @property
    def _city(self):
        city, _ = City.objects.get_or_create(
            name=self._data["city"]
        )
        return city

    def _send_mail_promo_code(self):
        # Кинуть для админа сообщение на почту с информацией,
        # что текущая медсестра воспользовалась промокодом пользователя такого-то
        pass

    def _create_personal_promo_code(self):
        self.result.promo_code = f"{self._nurse.id}{get_random_string(length=5)}"
        self.result.save()
        # Кинуть для этой медсестры сообщение на почту с её кодом
