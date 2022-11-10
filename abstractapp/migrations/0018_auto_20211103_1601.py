# Generated by Django 3.2.8 on 2021-11-03 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractapp', '0017_auto_20211025_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_data',
            field=models.DateField(default=datetime.date(2021, 11, 3)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 11, 3, 16, 1, 56, 33282)),
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Vegitables', 'Vegitables'), ('Womens Clothes', 'Womans Clothes'), ('Mens Clothes', 'Mens Clothes')], max_length=20),
        ),
    ]