from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    pass


@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    pass


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    pass


@admin.register(Includes)
class IncludeAdmin(admin.ModelAdmin):
    pass


@admin.register(Excludes)
class ExcludeAdmin(admin.ModelAdmin):
    pass


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    pass


@admin.register(Entertainment)
class EntertainmentAdmin(admin.ModelAdmin):
    pass
