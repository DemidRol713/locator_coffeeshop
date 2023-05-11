# Generated by Django 4.1 on 2022-10-12 13:50

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('article', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
            ],
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
