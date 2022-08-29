from django.db import models

from coffeeshop.models import CoffeeShop


# Create your models here.
class Drink(models.Model):
    """
    Класс Напиток
    """
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    # tags = models
    id_coffee_house = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    grade = models.FloatField()