from .models import Accommodation, AccommodationRating

from common.exceptions import ObjectNotFoundException


class AccommodationService:
    model = Accommodation
    rating = AccommodationRating

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.select_related('city').select_related('location')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException("Hotels not found")
