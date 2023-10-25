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


