from django.db import models

from models_app.models import Product


class ProductPrice(models.Model):
    price = models.PositiveIntegerField(verbose_name="Цена")
    discount_price = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Цена со скидкой"
    )
    city = models.ForeignKey(
        "City",
        on_delete=models.CASCADE,
        related_name="prices_city",
        verbose_name="Город"
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="prices_product",
        verbose_name="Продукт"
    )

    @staticmethod
    def price_in_city(product: Product, city_localization: str):
        return ProductPrice.objects.get(
            product=product,
            city__localization=city_localization
        ).price

    def __str__(self):
        return f"{self.id} - {self.price} - {self.city.name}"

    class Meta:
        db_table = "product_pricies"
        unique_together = ["product", "city"]
        verbose_name = "Цена на продукт"
        verbose_name_plural = "Цены на продукты"
