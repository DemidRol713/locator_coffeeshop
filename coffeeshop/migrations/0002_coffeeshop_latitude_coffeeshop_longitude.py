# Generated by Django 4.1 on 2022-09-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeshop',
            name='latitude',
            field=models.FloatField(default=59.938732),
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='longitude',
            field=models.FloatField(default=30.316229),
        ),
    ]