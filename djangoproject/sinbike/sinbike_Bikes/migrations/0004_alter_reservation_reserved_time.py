# Generated by Django 3.2.5 on 2021-07-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_Bikes', '0003_alter_bike_reserved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reserved_time',
            field=models.DateTimeField(),
        ),
    ]
