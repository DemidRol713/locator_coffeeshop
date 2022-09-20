from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """

    """

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def get_user_by_id(self, id:int):
        """

        :param id:int
        :return: User
        """
        return super().get_queryset().get(id=id)