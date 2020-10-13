# Generated by Django 3.0.8 on 2020-10-13 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='lease_owner',
        ),
        migrations.AlterField(
            model_name='day',
            name='date_created',
            field=models.DateField(default=datetime.date(2020, 10, 13), editable=False),
        ),
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.DateField(default=datetime.date(2020, 10, 14)),
        ),
    ]
