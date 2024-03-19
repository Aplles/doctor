from django.db import models


class Currency(models.Model):
    currency = models.CharField(max_length=30, verbose_name="Валюта")

    def __str__(self):
        return f"{self.id} - {self.currency}"

    class Meta:
        db_table = "currencies"
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"
