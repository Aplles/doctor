# Generated by Django 4.0 on 2024-03-19 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0008_alter_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=30, verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
                'db_table': 'currencies',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='city',
            name='localization',
            field=models.CharField(default=0, max_length=100, verbose_name='Локализация'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='product',
            field=models.ManyToManyField(related_name='cities_product', to='models_app.Product', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='models_app.Category', verbose_name='Категории'),
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('discount_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена со скидкой')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices_currency', to='models_app.currency', verbose_name='Валюта')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices_product', to='models_app.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Цена на продукт',
                'verbose_name_plural': 'Цены на продукты',
                'db_table': 'product_pricies',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('localization', models.CharField(max_length=3, verbose_name='Локализация')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries_currency', to='models_app.currency', verbose_name='Валюта')),
                ('default_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries_city', to='models_app.city', verbose_name='Город по умолчанию')),
                ('products', models.ManyToManyField(related_name='countries', to='models_app.Product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'db_table': 'countries',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='cities_country', to='models_app.country', verbose_name='Город по умолчанию'),
            preserve_default=False,
        ),
    ]
