# Generated by Django 3.2.5 on 2021-07-31 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_Customers', '0015_trip_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.CharField(default='ongoing', max_length=16),
        ),
    ]