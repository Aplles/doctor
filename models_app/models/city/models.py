from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    is_approved = models.BooleanField(default=False, verbose_name="Одобренный")

    class Meta:
        db_table = "cities"
        verbose_name = "Город"
        verbose_name_plural = "Города"
