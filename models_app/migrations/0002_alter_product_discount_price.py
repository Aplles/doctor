# Generated by Django 4.0 on 2024-02-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена со скидкой'),
        ),
    ]
