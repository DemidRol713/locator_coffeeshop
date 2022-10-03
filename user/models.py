from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .user_manager import UserManager


# Create your models here.
class Profile(AbstractUser):
    """
    Класс Пользователь(дополнение к стандартной модели пользователя в Django)
    """
    image = models.ImageField(default='/static/img/avatars/avatar.jpg')
    date_of_birth = models.DateField(default=timezone.now)
    manager = UserManager()