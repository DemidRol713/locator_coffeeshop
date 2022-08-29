import os.path

from django.db import models
from locator_coffeeshop import settings
from settings_coffee_shop.models import SettingsCoffeeShop

# Create your models here.
# def get_files_path():
#     return os.path.join(settings.DATA_FOLDER, "coffeeshop")

class File(models.Model):
    """
    Класс Файл
    """
    name = models.CharField(max_length=50)
    path = models.FilePathField(path=settings.DATA_FOLDER)
    id_setting = models.ForeignKey(SettingsCoffeeShop, on_delete=models.CASCADE)

