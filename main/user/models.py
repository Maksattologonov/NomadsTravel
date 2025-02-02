from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from accommodation.models import Accommodation
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


class Employee(models.Model):
    LANG_LEVELS = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    ]

    first_name = models.CharField(max_length=100, verbose_name=_('Имя'))
    last_name = models.CharField(max_length=100, verbose_name=_('Фамилия'))
    photo = models.ImageField(upload_to='employees/', verbose_name=_('Фото'))
    description = models.TextField(verbose_name=_('Описание'))
    slogan = models.CharField(max_length=200, verbose_name=_('Слоган'))
    slogan_author = models.CharField(max_length=100, verbose_name=_('Автор слогана'), blank=True)
    email = models.EmailField(verbose_name=_('Почта'))
    phone = models.CharField(max_length=20, verbose_name=_('Номер телефона'),
                             help_text='только в международном формате, например +996***')
    telegram = models.CharField(max_length=50, verbose_name=_('Telegram'), blank=True)
    passport_scan = models.FileField(upload_to='documents/', verbose_name=_('Скан паспорта'), blank=True, null=True)
    driver_license = models.FileField(upload_to='documents/', verbose_name=_('Скан вод. удостоверения'), blank=True, null=True)
    birth_place = models.CharField(max_length=100, verbose_name=_('Место рождения'))
    education = models.TextField(verbose_name=_('Образование'))
    languages = models.JSONField(verbose_name=_('Языки'))
    experience = models.IntegerField(verbose_name=_('Опыт'))

    class Meta:
        abstract = True


class Guide(Employee):
    history_knowledge_level = models.CharField(max_length=50, verbose_name=_('Уровень знания истории'))
    driving_experience = models.IntegerField(default=0, verbose_name=_('Опыт вождения'))

    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HotelEmployee(Employee):
    hotel = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    booking_name = models.CharField(max_length=100, verbose_name=_('Имя Фамилия сотрудника для брони'))
    contact_for_clients = models.CharField(max_length=100, verbose_name=_('Контакты'))

    class Meta:
        verbose_name = 'Работник отеля'
        verbose_name_plural = 'Работники отелей'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class OtherEmployee(Employee):
    role = models.CharField(max_length=100, verbose_name=_('Роль'))

    class Meta:
        verbose_name = 'Сторудник'
        verbose_name_plural = 'Другие сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
