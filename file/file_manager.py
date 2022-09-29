from django.db import models


class FileManager(models.Manager):

    def get_files_by_id_setting(self, id_setting):

        return super().get_queryset().filter(id_setting_id=id_setting)