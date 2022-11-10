# Generated by Django 3.2.8 on 2021-11-04 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractapp', '0021_auto_20211104_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 11, 4, 11, 30, 4, 195906)),
        ),
        migrations.AlterField(
            model_name='product',
            name='prize',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
        ),
    ]
