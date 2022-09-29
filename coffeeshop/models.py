from django.db import models
from django.contrib.postgres.fields import ArrayField


from coffeeshop.coffeeshop_manager import CoffeeShopManager


# Create your models here.
class CoffeeShop(models.Model):
    """
    Класс Кофейня
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    description = models.TextField()
    longitude = models.FloatField(default=30.316229)
    latitude = models.FloatField(default=59.938732)
    website = models.URLField(default='https://vk.com/feed')
    opening_hours = models.CharField(max_length=15, default='8:00 - 22:00')
    social_networks = ArrayField(
        models.URLField(),
        default=list
    )

    manager = CoffeeShopManager()