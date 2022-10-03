from django.db import models


class SettingsCoffeeshopManager(models.Manager):

    def get_settings_by_id_coffeeshop(self, id_coffeeshop):

        return super().get_queryset().get(id_coffeeshop_id=id_coffeeshop)