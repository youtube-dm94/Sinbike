# Generated by Django 3.2.5 on 2021-07-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_Customers', '0008_auto_20210713_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(default='', upload_to='avatars'),
        ),
    ]
