from django.db import models


class Nurse(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=16, verbose_name="Номер телефона")
    email = models.EmailField(max_length=255)
    promo_code = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Промокод"
    )
    certificate = models.ImageField(
        upload_to="nurses/certificates/%Y/%m/%d/",
        verbose_name="Изображение сертификата"
    )
    photo_with_passport = models.ImageField(
        upload_to="nurses/photo_with_passport/%Y/%m/%d/",
        verbose_name="Изображение селфи с паспортом"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    city = models.ForeignKey(
        "City",
        on_delete=models.SET_NULL,
        related_name="nurses",
        blank=True,
        null=True,
        verbose_name="Город"
    )

    class Meta:
        db_table = "nurses"
        verbose_name = "Медсестра"
        verbose_name_plural = "Медсестры"
