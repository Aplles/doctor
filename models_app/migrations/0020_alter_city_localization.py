# Generated by Django 4.0 on 2024-03-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0019_rename_product_city_products_alter_productprice_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='localization',
            field=models.CharField(max_length=100, unique=True, verbose_name='Локализация'),
        ),
    ]
