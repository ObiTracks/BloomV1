# Generated by Django 3.0.8 on 2020-09-05 18:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0018_auto_20200904_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timeslot_set', to='reservations.Day'),
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(default=datetime.date(2020, 9, 6)),
        ),
        migrations.AlterField(
            model_name='day',
            name='date_created',
            field=models.DateField(default=datetime.date(2020, 9, 5)),
        ),
    ]
