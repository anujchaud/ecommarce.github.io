# Generated by Django 3.2.8 on 2021-11-04 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractapp', '0022_auto_20211104_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 11, 4, 11, 31, 8, 648988)),
        ),
        migrations.AlterField(
            model_name='product',
            name='prize',
            field=models.BigIntegerField(max_length=5),
        ),
    ]