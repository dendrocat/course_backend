from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, login, password, **extra_fields):
        if not login:
            raise ValueError(_("The Login must be set"))
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault("username", login)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(login, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    login = models.CharField("Логин", max_length=150, blank=False, unique=True)
    password = models.CharField(_("password"), max_length=128, blank=False)

    username = models.CharField(_("username"), max_length=150, blank=False, null=False)

    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_superuser = models.BooleanField(_("superuser status"), default=False)

    USERNAME_FIELD = "login"

    objects = UserManager()

    def __str__(self):
        return "Пользователь: " + self.username.__str__()
