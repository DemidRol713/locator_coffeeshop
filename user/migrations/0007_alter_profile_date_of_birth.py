# Generated by Django 4.1 on 2022-09-05 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 9, 5, 10, 48, 15, 809581)),
        ),
    ]
