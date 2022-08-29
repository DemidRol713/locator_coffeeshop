from django.db import models
from coffeeshop.models import CoffeeShop


# Create your models here.
class SettingsCoffeeShop(models.Model):
    """
    Класс Настройки кофейни
    """
    id_coffee_house = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    type_content = models.CharField(max_length=40)
    # tags = models.ExpressionList