from django import forms
from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import path
from django.utils.safestring import mark_safe
from django_admin_geomap import ModelAdmin

from django.urls import reverse
from .forms import TourDayForm
from .models import *


class CityImageInlineAdmin(admin.TabularInline):
    model = CityImage


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    inlines = [CityImageInlineAdmin]


class RegionImageInlineAdmin(admin.TabularInline):
    model = RegionImage


class DestinationImageInlineAdmin(admin.TabularInline):
    model = DestinationImages


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


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines = [DestinationImageInlineAdmin]

class TourDayOrderInline(admin.TabularInline):
    model = TourDayOrder
    extra = 1  # Количество пустых форм для добавления новых дней

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourDayOrderInline]
    list_display = ('name', 'date_start', 'duration')
    search_fields = ('name', 'description')

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


class ActivityImageInlineAdmin(admin.TabularInline):
    model = ActivityImage

@admin.register(Activity)
class ActivityAdmin(ModelAdmin):
    inlines = [ActivityImageInlineAdmin]


class TransportDistanceInline(admin.TabularInline):
    model = TransportDistance
    extra = 1

@admin.register(TourDay)
class TourDayAdmin(admin.ModelAdmin):
    list_display = ('name', 'weather', 'total_distance')
    readonly_fields = ('generate_weather_button', 'total_distance')
    inlines = [TransportDistanceInline]

    def generate_weather_button(self, obj):
        if obj.id:
            url = reverse('admin:generate-weather', args=[obj.id])
            return mark_safe(f'<a class="button" href="{url}">🔄 Генерация погоды</a>')
        return "Сохраните запись, чтобы сгенерировать погоду"

    generate_weather_button.short_description = "Генерация погоды"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<path:object_id>/generate-weather/',
                self.admin_site.admin_view(self.generate_weather_action),
                name='generate-weather',
            ),
        ]
        return custom_urls + urls

    def generate_weather_action(self, request, object_id):
        obj = self.get_object(request, object_id)
        if not obj:
            self.message_user(request, "Ошибка: запись не найдена", messages.ERROR)
            return redirect(request.META.get('HTTP_REFERER', 'admin:index'))

        if not obj.destination.exists():
            self.message_user(request, "Ошибка: нет пункта назначения", messages.ERROR)
            return redirect(request.META.get('HTTP_REFERER', 'admin:index'))

        try:
            obj.fetch_weather()
            self.message_user(request, f"Погода обновлена: {obj.weather}", messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"Ошибка при обновлении погоды: {str(e)}", messages.ERROR)

        return redirect(request.META.get('HTTP_REFERER', 'admin:index'))