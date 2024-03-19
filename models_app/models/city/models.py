from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    is_approved = models.BooleanField(default=False, verbose_name="Одобренный")
    localization = models.CharField(max_length=100, verbose_name="Локализация")
    country = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        related_name="cities_country",
        verbose_name="Страна"
    )
    product = models.ManyToManyField(
        "Product",
        related_name="cities_product",
        verbose_name="Продукты"
    )

    def __str__(self):
        return f"{self.name} - {self.is_approved}"

    class Meta:
        db_table = "cities"
        verbose_name = "Город"
        verbose_name_plural = "Города"
