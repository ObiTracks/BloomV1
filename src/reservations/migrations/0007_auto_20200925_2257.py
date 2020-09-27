# Generated by Django 3.0.8 on 2020-09-26 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_auto_20200925_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='party_members',
        ),
        migrations.AddField(
            model_name='reservation',
            name='party_members',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]