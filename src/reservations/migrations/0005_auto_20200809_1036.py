# Generated by Django 3.0.8 on 2020-08-09 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20200809_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='day_after_field',
        ),
        migrations.AddField(
            model_name='day',
            name='day',
            field=models.DateField(default=datetime.date(2020, 8, 9)),
        ),
        migrations.AddField(
            model_name='day',
            name='day_after',
            field=models.DateField(default=datetime.date(2020, 8, 10)),
        ),
    ]