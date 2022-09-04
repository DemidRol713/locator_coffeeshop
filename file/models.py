import os.path

from django.db import models
from locator_coffeeshop import settings
from settings_coffeeshop.models import SettingsCoffeeShop


class File(models.Model):
    """
    Класс Файл
    """
    name = models.CharField(max_length=50)
    path = models.FilePathField(path=settings.DATA_FOLDER)
    id_setting = models.ForeignKey(SettingsCoffeeShop, on_delete=models.CASCADE)

