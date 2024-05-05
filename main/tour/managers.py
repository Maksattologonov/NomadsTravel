from django.db import models
from django.utils.translation import gettext_lazy as _
from django_admin_geomap import GeoItem


class Location(models.Model, GeoItem):
    name = models.CharField(max_length=100, verbose_name=_("Название локации"))
    lon = models.FloatField(verbose_name=_("Долгота"))
    lat = models.FloatField(verbose_name=_("Широта"))

    @property
    def geomap_popup_view(self):
        """Html code for display in marker popup at the map for RO users."""
        return "<strong>{}</strong>".format(escape(str(self), quote=True))

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
        """Must return longitude of object as string."""
        raise NotImplementedError("{}.geomap_longitude".format(self.__class__.__name__))

    @property
    def geomap_latitude(self):
        """Must return latitude of object as string."""
        raise NotImplementedError("{}.geomap_latitude".format(self.__class__.__name__))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'locations'
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


