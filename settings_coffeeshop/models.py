from django.contrib.postgres.fields import ArrayField
from django.db import models

from coffeeshop.models import CoffeeShop
from settings_coffeeshop.settings_coffeeshop_manager import SettingsCoffeeshopManager


def get_tags_default():
    """
    Возвращает значение tags по умолчанию
    :return:
    """
    return list()

def get_images_default():
    """
    Возвращает значение images по умолчанию
    :return:
    """

    return ['static/img/photos/']
# Create your models here.
class SettingsCoffeeShop(models.Model):
    """
    Класс Настройки кофейни
    """
    id_coffeeshop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    type_content = models.CharField(max_length=40)
    tags = ArrayField(
        models.CharField(max_length=30),
        default=get_tags_default,
        blank=False
    )

    images = ArrayField(
        models.ImageField(),
        default=get_images_default,
        blank=False
    )
    manager = SettingsCoffeeshopManager()