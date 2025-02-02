from django.contrib import admin
from .models import Guide, HotelEmployee, OtherEmployee


@admin.register(Guide)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelEmployee)
class CategoryAdmin(admin.ModelAdmin):
    pass



@admin.register(OtherEmployee)
class CategoryAdmin(admin.ModelAdmin):
    pass

