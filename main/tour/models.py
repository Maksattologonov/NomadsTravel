from django.db import models
from django.utils.translation import gettext_lazy as _


class Hotel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название сайта'))
    city = models.CharField(max_length=255, verbose_name=_('Город'))


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название города'))
    region = models.CharField()


class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название области'))
    description = models.TextField(verbose_name=_('Описание'))
    image = models.FileField(upload_to='regions', verbose_name=_('Изображение'))