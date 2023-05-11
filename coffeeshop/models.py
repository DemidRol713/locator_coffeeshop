from django.db import models
from django.contrib.postgres.fields import ArrayField

from coffeeshop.coffeeshop_manager import CoffeeShopManager


def get_website_default():
    """
    Возвращает значение website по умолчанию
    :return:
    """
    return ['https://vk.com/feed']


def get_email_default():
    """
    Возвращает значение email по умолчанию
    :return:
    """
    return ['test@test.test']


def get_social_networks_default():
    """
    Возвращает значение social_networks по умолчанию
    :return:
    """
    return ['https://vk.com']

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

    return ['static/img/photos/no_photo.png']


# Create your models here.
class CoffeeShop(models.Model):
    """
    Класс Кофейня
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    description = models.TextField()
    longitude = models.FloatField(default=30.316229)
    latitude = models.FloatField(default=59.938732)
    website = ArrayField(models.URLField(), default=get_website_default)
    opening_hours = models.TextField(default='8:00 - 22:00')
    telephone = ArrayField(models.CharField(max_length=200))
    email = ArrayField(
        models.EmailField(),
        default=get_email_default
    )
    social_networks = ArrayField(
        models.URLField(),
        default=get_social_networks_default
    )
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

    manager = CoffeeShopManager()
