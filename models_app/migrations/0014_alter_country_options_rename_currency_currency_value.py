# Generated by Django 4.0 on 2024-03-19 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0013_alter_city_product_alter_country_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['id'], 'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='currency',
            new_name='value',
        ),
    ]
