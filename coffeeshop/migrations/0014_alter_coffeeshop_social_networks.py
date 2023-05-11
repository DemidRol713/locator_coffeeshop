# Generated by Django 4.1 on 2022-11-02 14:11

import coffeeshop.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0013_alter_coffeeshop_email_alter_coffeeshop_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeeshop',
            name='social_networks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=coffeeshop.models.get_social_networks_default, size=None),
        ),
    ]
