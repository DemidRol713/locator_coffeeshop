from django.db import models


class SettingsCoffeeshopManager(models.Manager):

    def get_settings_by_id_coffeeshop(self, id_coffeeshop):

        setting = super().get_queryset().filter(id_coffeeshop_id=id_coffeeshop)
        if setting is not None:
            return setting