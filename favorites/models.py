from django.db import models

from user.models import Profile

# Create your models here.
class Favorites(models.Model):
    """
    Класс Избранные
    """
    id_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # coffee_shop_list = models