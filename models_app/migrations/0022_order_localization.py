# Generated by Django 4.0 on 2024-04-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0021_country_localization'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='localization',
            field=models.CharField(default='-', max_length=100, verbose_name='Локализация'),
        ),
    ]
