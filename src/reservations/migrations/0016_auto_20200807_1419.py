# Generated by Django 3.0.8 on 2020-08-07 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0015_auto_20200807_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('apt_number', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('lease_members', models.ManyToManyField(blank=True, related_name='_resident_lease_members_+', to='reservations.Resident')),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='reservation',
            name='resident',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resident', to='reservations.Resident'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='party_members',
            field=models.ManyToManyField(blank=True, related_name='party_members', to='reservations.Resident'),
        ),
    ]
