# Generated by Django 3.0.8 on 2020-08-09 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_auto_20200809_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='day',
            name='nextday',
        ),
        migrations.AddField(
            model_name='day',
            name='day_created',
            field=models.DateField(default=datetime.date(2020, 8, 9)),
        ),
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.DateField(default=datetime.date(2020, 8, 10)),
        ),
    ]
