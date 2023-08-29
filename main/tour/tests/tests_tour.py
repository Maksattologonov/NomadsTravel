from django.core.files.base import ContentFile
from rest_framework.test import APITestCase
from django.urls import reverse

from tour.apis import HotelSerializer
from tour.models import *


class TestTourView(APITestCase):
    def setUp(self) -> None:
        location = Location.objects.create(name='Бишкек', lon=70.3131, lat=43.2312)
        country = Country.objects.create(name='Кыргызстан', description='Spme descr', location=location.name)
        country_image = CountryImage.create(country_id=country.name, image=ContentFile(b"../../media/countries/"))
        region = Region.objects.create(name='Чуй',
                                       description="Lorem ipsum dolor amet",
                                       country=country)
        region_image = RegionImage.create(region_id=region.name, image=ContentFile(b"../../media/countries/"))
        city = City.objects.create(name='Бишкек',
                                   region=region)
        city_image = RegionImage.create(city_id=city.name, image=ContentFile(b"../../media/countries/"))
        Accommodation.objects.create()

    def test_get(self):
        url = reverse('tour')

        response = self.client.get(url)
        self.assertEquals(HotelSerializer())
