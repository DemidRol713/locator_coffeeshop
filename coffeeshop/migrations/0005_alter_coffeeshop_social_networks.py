# Generated by Django 4.1 on 2022-09-23 13:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0004_coffeeshop_opening_hours_coffeeshop_social_networks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeeshop',
            name='social_networks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=list, size=None),
        ),
    ]