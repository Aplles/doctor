from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=18, verbose_name="Номер телефона")
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Адрес"
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    direction_image = models.ImageField(
        upload_to="orders/direction_image/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Изображение с направлением"
    )
    delivery = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Доставка"
    )
    localization = models.CharField(
        max_length=100,
        default='-',
        verbose_name="Локализация"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    products = models.ManyToManyField(
        'Product',
        through='ProductAmount',
        verbose_name='Продукты',
    )

    def __str__(self):
        return f"{self.first_name} - {self.phone}"

    class Meta:
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
