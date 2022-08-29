from django.db import models


# Create your models here.
class CoffeeShop(models.Model):
    """
    Класс Кофейня
    """
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    description = models.TextField()