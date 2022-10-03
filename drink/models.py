from django.db import models
from django.contrib.postgres.fields import ArrayField

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
    tags = ArrayField(
        models.CharField(max_length=30)
    )
    id_coffeeshop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    grade = models.FloatField()