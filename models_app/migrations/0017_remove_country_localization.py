# Generated by Django 4.0 on 2024-03-20 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0016_remove_productprice_currency_productprice_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='localization',
        ),
    ]