# Generated by Django 3.0.8 on 2020-09-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_auto_20200926_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='lease_members',
        ),
    ]