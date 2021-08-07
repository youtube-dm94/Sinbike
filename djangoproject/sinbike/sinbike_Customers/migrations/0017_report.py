# Generated by Django 3.2.5 on 2021-08-01 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_Customers', '0016_trip_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('subject', models.TextField()),
                ('body', models.TextField()),
                ('attachments', models.ImageField(default='', upload_to='reports')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sinbike_Customers.customer')),
            ],
        ),
    ]