from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(
        upload_to="products/image/%Y/%m/%d/",
        verbose_name="Изображение"
    )
    price = models.PositiveIntegerField(verbose_name="Цена")
    discount_price = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Цена со скидкой"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория"
    )

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
