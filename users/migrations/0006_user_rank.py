# Generated by Django 3.1 on 2020-08-10 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200809_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.IntegerField()),
                ('age', models.IntegerField()),
                ('orientation', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('disability', models.IntegerField()),
                ('education', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
