# Generated by Django 4.1 on 2022-10-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0005_alter_coffeeshop_social_networks'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeshop',
            name='telephone',
            field=models.CharField(default='88005553535', max_length=15),
        ),
    ]
