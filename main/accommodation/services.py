from accommodation.models import Accommodation
from common.exceptions import ObjectNotFoundException


class AccommodationService:
    model = Accommodation

    @classmethod
    def get_accommodations(cls, **filters):
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Accommodation not found')
        