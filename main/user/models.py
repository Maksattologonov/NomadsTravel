from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name=_("Почта"))
    full_name = models.CharField(max_length=255, verbose_name=_("Полное имя"))
    username = models.CharField(max_length=30, unique=True, verbose_name=_("Никнейм"))
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name=_("Аватар"))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']

    def __str__(self):
        return self.email
