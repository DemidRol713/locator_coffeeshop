# Generated by Django 4.1 on 2022-09-21 16:26

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('settings_coffeeshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='settingscoffeeshop',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
