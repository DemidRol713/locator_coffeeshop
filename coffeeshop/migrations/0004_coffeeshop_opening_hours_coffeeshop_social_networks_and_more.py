# Generated by Django 4.1 on 2022-09-23 13:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0003_alter_coffeeshop_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeshop',
            name='opening_hours',
            field=models.CharField(default='8:00 - 22:00', max_length=15),
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='social_networks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(default='https://github.com/DemidRol713/locator_coffeeshop'), default=['https://github.com/DemidRol713/locator_coffeeshop'], size=None),
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='website',
            field=models.URLField(default='https://vk.com/feed'),
        ),
    ]