# Generated by Django 3.2.5 on 2021-07-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_Customers', '0007_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='promo',
            field=models.FloatField(default=0.0),
        ),
    ]