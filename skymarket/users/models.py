from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager


class UserRoles:
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    pass
