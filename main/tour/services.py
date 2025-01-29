from django.db import IntegrityError
from django.db.models import Q

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
            return cls.model.objects.filter(**filters).prefetch_related('tour_id').prefetch_related('activity')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Destination not found')

    @classmethod
    def get_query_param(cls, request):
        filters = Q()

        tour_id = request.GET.get('tour_id')
        if tour_id:
            filters &= Q(pk__in=tour_id.split(','))
        print(filters)

        country_id = request.GET.get('country_id')
        if country_id:
            filters &= Q(location__in=country_id.split(','))

        region_id = request.GET.get('region_id')
        if region_id:
            filters &= Q(region__in=region_id)

        hotel_id = request.GET.get('hotel_id')
        if hotel_id:
            filters &= Q(hotel_id__lte=hotel_id)
        print(filters)
        return cls.model.objects.filter(filters).distinct()

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
    def get(cls, request):
        filters = Q()

        tour_type_id = request.GET.get('tour_type_id')
        if tour_type_id:
            filters &= Q(tour_types__id__in=tour_type_id.split(','))

        promotion = request.GET.get('promotion')
        if promotion:
            filters &= Q(promotion__in=promotion.split(','))

        difficulty_from = request.GET.get('difficulty_from')
        if difficulty_from:
            filters &= Q(difficulty__gte=difficulty_from)

        difficulty_to = request.GET.get('difficulty_to')
        if difficulty_to:
            filters &= Q(difficulty__lte=difficulty_to)

        countries_id = request.GET.get('countries_id')
        if countries_id:
            filters &= Q(countries__id__in=countries_id.split(','))

        from_date = request.GET.get('from_date')
        if from_date:
            filters &= Q(date_start__gte=from_date)

        to_date = request.GET.get('to_date')
        if to_date:
            filters &= Q(date_start__lte=to_date)

        min_price = request.GET.get('min_price')
        if min_price:
            filters &= Q(price__gte=float(min_price))

        max_price = request.GET.get('max_price')
        if max_price:
            filters &= Q(price__lte=float(max_price))

        min_days = request.GET.get('min_days')
        if min_days:
            filters &= Q(duration__gte=min_days)

        max_days = request.GET.get('max_days')
        if max_days:
            filters &= Q(duration__lte=max_days)

        return cls.model.objects.filter(filters).distinct()



class DestinationRouteService:
    model = DestinationRating

    @classmethod
    def save_rating(cls, pk: int, value: float):
        try:
            obj = cls.model.objects.create(destination=pk, value=value)
            obj.save()
        except IntegrityError:
            raise ObjectAlreadyExistsException("Rating already exists")

