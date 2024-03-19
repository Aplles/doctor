from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    localization = models.CharField(max_length=3, verbose_name="Локализация")
    currency = models.ForeignKey(
        "Currency",
        on_delete=models.CASCADE,
        related_name="countries_currency",
        verbose_name="Валюта"
    )
    default_city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        related_name="countries_city",
        verbose_name="Город по умолчанию"
    )
    products = models.ManyToManyField(
        "Product",
        related_name="countries",
        verbose_name="Продукты"
    )

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = "countries"
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
