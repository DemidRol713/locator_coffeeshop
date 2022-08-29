from django.db import models
from coffeeshop.models import CoffeeShop
from user.models import Profile


# Create your models here.
class Review(models.Model):
    """
    Класс Отзыв
    """
    id_coffee_house = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    grade = models.FloatField()