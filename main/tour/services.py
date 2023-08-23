from .models import Accommodation

from common.exceptions import ObjectNotFoundException


class HotelService:
    model = Accommodation

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException("Hotels not found")
