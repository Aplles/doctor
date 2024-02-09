from django.db import models


class ProductAmount(models.Model):
    amount = models.PositiveIntegerField(verbose_name="Количество")
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="product_amounts",
        verbose_name="Продукт"
    )
    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        related_name="product_amounts_order",
        verbose_name="Заказ"
    )

    class Meta:
        db_table = "product_amounts"
        verbose_name = "Количество продукта"
        verbose_name_plural = "Количество продуктов"
