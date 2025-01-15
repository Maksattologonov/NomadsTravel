from django.db import models
from django.utils.html import escape
from django.utils.translation import gettext_lazy as _
from django_admin_geomap import GeoItem


class Location(models.Model, GeoItem):
    TYPES = [
        ("country", "Страна"),
        ("region", "Область"),
        ("city", "Город"),
        ("destination", "Пункт"),
    ]
    name = models.CharField(max_length=100, verbose_name=_("Название локации"))
    type = models.CharField(max_length=100,choices=TYPES, verbose_name=_("Тип локации"))
    lon = models.FloatField(verbose_name=_("Долгота"))
    lat = models.FloatField(verbose_name=_("Широта"))

    @property
    def geomap_popup_view(self):
        """Html code for display in marker popup at the map for RO users."""
        return "<strong>{}</strong>".format(escape(str(self)))

    @property
    def geomap_popup_edit(self):
        """Html code for display in marker popup at the map for admin users."""
        return self.geomap_popup_view

    @property
    def geomap_popup_common(self):
        """Html code for display in marker popup at the map for common views."""
        return self.geomap_popup_view

    @property
    def geomap_icon(self):
        """Full url for marker icon at the map."""
        return self.default_icon

    @property
    def geomap_longitude(self):
        try:
            return self.lon
        except NotImplementedError:
            raise NotImplementedError("{}.geomap_longitude".format(self.__class__.__name__))

    @property
    def geomap_latitude(self):
        try:
            return self.lat
        except NotImplementedError:
            raise NotImplementedError("{}.geomap_latitude".format(self.__class__.__name__))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'locations'
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


