# Generated by Django 4.1 on 2022-09-01 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_date_of_birth_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 9, 1, 14, 41, 6, 834602)),
        ),
    ]