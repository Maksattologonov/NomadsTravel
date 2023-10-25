from .models import Accommodation, AccommodationRating, City

from common.exceptions import ObjectNotFoundException


class AccommodationService:
    model = Accommodation
    rating = AccommodationRating

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.filter(**filters).select_related('city').select_related('location')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException("Hotels not found")


class CityService:
    model = City

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.filter(**filters).select_related('location')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('City not found')
