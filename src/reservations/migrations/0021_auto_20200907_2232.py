# Generated by Django 3.0.8 on 2020-09-08 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0020_auto_20200907_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_email', models.EmailField(max_length=60)),
                ('address_line', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=1024, verbose_name='City')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP/Postal code')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Company Name',
                'ordering': ['-company_name'],
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.Company'),
        ),
    ]