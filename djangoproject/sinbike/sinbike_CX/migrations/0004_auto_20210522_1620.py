# Generated by Django 3.2 on 2021-05-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinbike_CX', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
