from .models import Accommodation, AccommodationRating

from common.exceptions import ObjectNotFoundException


class AccommodationService:
    model = Accommodation
    rating = AccommodationRating

    @classmethod
    def get(cls, **filters):
        try:
            return cls.rating.objects.select_related('target_content_type')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException("Hotels not found")
