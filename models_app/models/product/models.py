from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(
        upload_to="products/image/%Y/%m/%d/",
        verbose_name="Изображение"
    )
    category = models.ManyToManyField(
        "Category",
        related_name="products",
        verbose_name="Категории"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
