from functools import lru_cache


from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework.exceptions import NotFound
from service_objects.fields import DictField
from service_objects.services import ServiceOutcome
from service_objects.services import ServiceWithResult

from api.services.nurse.promo_code import NursePromoCodePresenceService
from conf.settings import smtp
from models_app.models import City
from models_app.models import Nurse


class NurseCreateService(ServiceWithResult):
    validated_data = DictField()

    custom_validations = ["_nurse_promo_code_presence"]

    def process(self):
        self.run_custom_validations()
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
        if "affiliate_program" in self._data:
            affiliate_program = self._data.pop("affiliate_program")
        if "promocode" in self._data:
            promo_code = self._data.pop("promocode")
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
        send_mail(
            subject='[!] OurDoctor',
            message=f"""
            Медсестра {self.result.first_name} 
            воспользовалась промокодом медсестры {self._nurse_for_promo.first_name}
            """,
            from_email=smtp.EMAIL_HOST_USER,
            recipient_list=[smtp.ADMIN_EMAIL_ADDRESS],
        )

    def _create_personal_promo_code(self):
        self.result.promo_code = f"{self.result.id}{get_random_string(length=5)}".upper()
        self.result.save()
        send_mail(
            subject='[!] OurDoctor',
            message=f"Ваш личный промокод: {self.result.promo_code}",
            from_email=smtp.EMAIL_HOST_USER,
            recipient_list=[self.result.email],
        )

    @property
    @lru_cache
    def _nurse_for_promo(self):
        return ServiceOutcome(
            NursePromoCodePresenceService,
            {"promo_code": self._data["promocode"]}
        ).result

    def _nurse_promo_code_presence(self):
        promo_code = self._data.get("promocode")
        if promo_code and not self._nurse_for_promo:
            raise NotFound("There is no such promo code")
