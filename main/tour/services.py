from .models import Accommodation, AccommodationRating, City, Destination

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


class DestinationService:
    model = Destination

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Destination not found')

    @classmethod
    def get_title(cls, **filters):
        try:
            return cls.model.objects.values('title', 'main_image')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Destination not found')
