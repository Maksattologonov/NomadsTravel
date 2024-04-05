from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import *


class AccommodationImageInline(admin.TabularInline):
    model = AccommodationImage


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    inlines = [AccommodationImageInline, ]


class CityImageInlineAdmin(admin.TabularInline):
    model = CityImage


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    inlines = [CityImageInlineAdmin]


class RegionImageInlineAdmin(admin.TabularInline):
    model = RegionImage


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    inlines = [RegionImageInlineAdmin]


class CountryImageInlineAdmin(admin.StackedInline):
    model = CountryImage


@admin.register(Country)
class CountyAdmin(admin.ModelAdmin):
    inlines = [CountryImageInlineAdmin]


@admin.register(Location)
class LocationAdmin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_height = "600px"
    geomap_default_longitude = "77.84343"
    geomap_default_latitude = "42.84343"
    geomap_default_zoom = '5'


@admin.register(AccommodationRating)
class AccommodationRatingAdmin(admin.ModelAdmin):
    pass


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour)
class TourAdmin(ModelAdmin):
    pass


@admin.register(TourComment)
class TourCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(TourRating)
class TourRatingAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeOfTour)
class TypeOfTourAdmin(admin.ModelAdmin):
    pass


@admin.register(DestinationRating)
class DestinationRatingAdmin(ModelAdmin):
    pass
