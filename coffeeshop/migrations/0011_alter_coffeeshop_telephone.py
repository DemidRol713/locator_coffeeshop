# Generated by Django 4.1 on 2022-11-01 15:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0010_alter_coffeeshop_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeeshop',
            name='telephone',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
    ]
