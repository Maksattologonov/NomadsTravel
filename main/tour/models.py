from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_admin_geomap import GeoItem


class Location(models.Model, GeoItem):
    name = models.CharField(max_length=100, verbose_name=_("Название локации"))
    lon = models.FloatField(verbose_name=_("Долгота"))
    lat = models.FloatField(verbose_name=_("Широта"))

    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'locations'
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Accommodation(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название отели'))
    description = models.TextField(verbose_name=_('Описание'))
    address = models.CharField(max_length=255, verbose_name=_('Адрес'))
    city = models.ForeignKey('City', on_delete=models.DO_NOTHING, max_length=255, verbose_name=_('Город'))
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, max_length=255, verbose_name=_('Локация'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'accommodations'
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class AccommodationRating(models.Model):
    target_content_type = models.ForeignKey(Accommodation, on_delete=models.CASCADE, verbose_name=_('Отель'))
    target_object_id = models.PositiveIntegerField()
    rating_value = models.PositiveIntegerField(default=0)
    total_ratings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Rating for {self.target_content_type.model} {self.target_object_id}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class AccommodationImage(models.Model):
    accommodation_id = models.ForeignKey('Accommodation', on_delete=models.DO_NOTHING, verbose_name=_('Отель'))
    image = models.ImageField(upload_to='accommodations', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'accommodation_images'
        verbose_name = 'Изображение отеля'
        verbose_name_plural = 'Изображение отелей'


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name=_("Локация"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class CityImage(models.Model):
    city_id = models.ForeignKey('City', on_delete=models.DO_NOTHING, verbose_name=_('Город'))
    image = models.ImageField(upload_to='cities', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'city_images'
        verbose_name = 'Изображение города'
        verbose_name_plural = 'Изображение городов'


class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name=_("Локация"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'regions'
        verbose_name = 'Область'
        verbose_name_plural = 'Области'


class RegionImage(models.Model):
    region_id = models.ForeignKey('Region', on_delete=models.DO_NOTHING, verbose_name=_('Регион'))
    image = models.ImageField(upload_to='regions', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'region_images'
        verbose_name = 'Изображение региона'
        verbose_name_plural = 'Изображение регионов'


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name=_("Локация"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'countries'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class CountryImage(models.Model):
    Country_id = models.ForeignKey('Country', on_delete=models.DO_NOTHING, verbose_name=_('Страна'))
    image = models.ImageField(upload_to='countries', verbose_name=_("Загрузить изображение"))

    def __str__(self):
        return str(self.image)

    class Meta:
        db_table = 'country_images'
        verbose_name = 'Изображение страны'
        verbose_name_plural = 'Изображение стран'
