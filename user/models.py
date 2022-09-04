from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):
    """
    Класс Пользователь(дополнение к стандартной модели пользователя в Django)
    """
    image = models.ImageField(default='/static/img/avatars/avatar.jpg')
    date_of_birth = models.DateField(default=datetime.now())