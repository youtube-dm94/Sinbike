# Generated by Django 2.2.14 on 2021-07-18 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_CX', '0005_alter_answer_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]