from django.db import models
from django.utils.translation import gettext_lazy as _


class Hotel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название отели'))
    city = models.CharField(max_length=255, verbose_name=_('Город'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название города'))
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название области'))
    description = models.TextField(verbose_name=_('Описание'))
    image = models.FileField(upload_to='regions', verbose_name=_('Изображение'))
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название страны'))
    image = models.FileField(upload_to='countries', verbose_name=_('Изображения'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
