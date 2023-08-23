from django.core.files.base import ContentFile
from rest_framework.test import APITestCase
from django.urls import reverse

from tour.apis import HotelSerializer
from tour.models import *


class TestTourView(APITestCase):
    def setUp(self) -> None:
        country = Country.objects.create(name='Кыргызстан',
                                         image=ContentFile(b"../../media/countries/", name="foo.png"))
        region = Region.objects.create(name='Чуй',
                                       description="Lorem ipsum dolor amet",
                                       image=ContentFile(b"../../media/countries/", name="foo.png"),
                                       country=country)
        city = City.objects.create(name='Бишкек',
                                   region=region)
        Accommodation.objects.create()

    def test_get(self):
        url = reverse('tour')

        response = self.client.get(url)
        self.assertEquals(HotelSerializer())
