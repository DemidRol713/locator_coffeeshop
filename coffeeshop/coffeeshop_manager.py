from django.db import models


class CoffeeShopManager(models.Manager):

    def get_coffeeshop_list(self):

        return super().get_queryset().all()

    def get_coffeeshop_by_id(self, id_coffeeshop):

        return super().get_queryset().get(id=id_coffeeshop)
