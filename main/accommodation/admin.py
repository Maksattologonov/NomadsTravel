from django.contrib import admin
from .models import *


class AccommodationImageInline(admin.TabularInline):
    model = AccommodationImage


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    inlines = [AccommodationImageInline]
    readonly_fields = ['elevation',]
