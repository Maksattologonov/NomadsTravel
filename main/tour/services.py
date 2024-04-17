from django.db import IntegrityError

from accommodation.models import Accommodation, AccommodationRating
from .models import City, Destination, Tour, DestinationRating

from common.exceptions import ObjectNotFoundException, ObjectAlreadyExistsException


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
            return cls.model.objects.filter(**filters).prefetch_related('tour').prefetch_related('activity')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Destination not found')

    @classmethod
    def filter(cls, **filters):
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


class TourService:
    model = Tour

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Tour not found')


class DestinationRouteService:
    model = DestinationRating

    @classmethod
    def save_rating(cls, pk: int, value: float):
        try:
            obj = cls.model.objects.create(destination=pk, value=value)
            obj.save()
        except IntegrityError:
            raise ObjectAlreadyExistsException("Rating already exists")