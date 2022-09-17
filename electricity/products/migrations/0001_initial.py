# Generated by Django 4.1 on 2022-08-30 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductParsed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_number', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('unit_measurement_price', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Спарсенный продукт',
                'verbose_name_plural': 'Спарсенные продукты',
            },
        ),
        migrations.CreateModel(
            name='StoreProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_number', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('unit_measurement_price', models.CharField(max_length=30)),
                ('quantity_in_store', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Наш товар',
                'verbose_name_plural': 'Наши товары',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='ParsValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('detailed_time_created', models.TimeField(auto_now_add=True)),
                ('url_root', models.URLField()),
                ('category', models.CharField(max_length=255)),
                ('Worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.worker')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productparsed')),
            ],
            options={
                'verbose_name': 'Парсинг лист',
                'verbose_name_plural': 'Парсинг листы',
            },
        ),
    ]