# Generated by Django 3.0.8 on 2020-08-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200804_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='disability',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
