# Generated by Django 3.2.5 on 2021-07-12 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_Customers', '0003_auto_20210712_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['created_at']},
        ),
    ]