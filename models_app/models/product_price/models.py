from django.db import models


class ProductPrice(models.Model):
    price = models.PositiveIntegerField(verbose_name="Цена")
    discount_price = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Цена со скидкой"
    )
    currency = models.ForeignKey(
        "Currency",
        on_delete=models.CASCADE,
        related_name="prices_currency",
        verbose_name="Валюта"
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="prices_product",
        verbose_name="Продукт"
    )

    def __str__(self):
        return f"{self.id} - {self.price} - {self.currency}"

    class Meta:
        db_table = "product_pricies"
        verbose_name = "Цена на продукт"
        verbose_name_plural = "Цены на продукты"
