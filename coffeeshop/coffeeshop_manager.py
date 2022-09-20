from django.db import models


class CoffeeShopManager(models.Manager):

    def get_coffeeshop_list(self):

        return super().get_queryset().all()