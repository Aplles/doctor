from django.db import models


class Currency(models.Model):
    value = models.CharField(max_length=30, unique=True, verbose_name="Валюта")

    def __str__(self):
        return f"{self.id} - {self.value}"

    class Meta:
        db_table = "currencies"
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"
