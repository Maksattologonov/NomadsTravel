from categories.models import Category
from common.exceptions import ObjectNotFoundException


class CategoryService:
    model = Category

    @classmethod
    def get_categories(cls, **filters):
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Category not found')
