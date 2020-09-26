# Generated by Django 3.0.8 on 2020-09-26 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20200925_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='party_members',
        ),
        migrations.AddField(
            model_name='reservation',
            name='party_members',
            field=models.ManyToManyField(blank=True, null=True, to='reservations.LeaseMember'),
        ),
    ]
