from django.contrib.postgres.fields import ArrayField
from django.db import models

from user.models import Profile
from coffeeshop.models import CoffeeShop


# Create your models here.
class Favorite(models.Model):
    """
    Класс Избранные
    """
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    coffeeshop_list = ArrayField(
        models.IntegerField()
    )