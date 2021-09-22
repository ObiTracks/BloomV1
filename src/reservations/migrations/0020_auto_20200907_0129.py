# Generated by Django 3.0.8 on 2020-09-07 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0019_customer_lease_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='lease_owner',
            field=models.ForeignKey(blank=True, default=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.Customer'),
        ),
    ]