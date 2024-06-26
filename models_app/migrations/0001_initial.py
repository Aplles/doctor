# Generated by Django 4.0 on 2024-02-09 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Одобренный')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=16, verbose_name='Номер телефона')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('direction_image', models.ImageField(blank=True, null=True, upload_to='orders/direction_image/%Y/%m/%d/', verbose_name='Изображение с направлением')),
                ('delivery', models.CharField(max_length=255, verbose_name='Доставка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='products/image/%Y/%m/%d/', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('discount_price', models.PositiveIntegerField(verbose_name='Цена со скидкой')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='models_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_amounts_order', to='models_app.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_amounts', to='models_app.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Количество продукта',
                'verbose_name_plural': 'Количество продуктов',
                'db_table': 'product_amounts',
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=16, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=255)),
                ('promo_code', models.CharField(blank=True, max_length=30, null=True, verbose_name='Промокод')),
                ('certificate', models.ImageField(upload_to='nurses/certificates/%Y/%m/%d/', verbose_name='Изображение сертификата')),
                ('photo_with_passport', models.ImageField(upload_to='nurses/photo_with_passport/%Y/%m/%d/', verbose_name='Изображение селфи с паспортом')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nurses', to='models_app.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Медсестра',
                'verbose_name_plural': 'Медсестры',
                'db_table': 'nurses',
            },
        ),
    ]
