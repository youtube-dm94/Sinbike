# Generated by Django 3.2.5 on 2021-07-12 18:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_Customers', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='sinbike_Customers.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credits',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.BinaryField(),
        ),
    ]