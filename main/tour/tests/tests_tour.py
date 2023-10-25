import json
import unittest.mock

from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from tour.apis import AccommodationSerializer
from tour.models import *


class TestTourView(APITestCase):
    def setUp(self) -> None:
        location = Location.objects.create(name='Бишкек', lon=70.3131, lat=43.2312)
        country = Country.objects.create(name='Кыргызстан', description='Spme descr', location=location)
        CountryImage.objects.create(country_id=country, image=ContentFile(b"../../media/countries/foo.jpg"))
        region = Region.objects.create(name='Чуй',
                                       description="Lorem ipsum dolor amet",
                                       country=country,
                                       location=location)
        RegionImage.objects.create(region_id=region, image=ContentFile(b"../../media/countries/foo.jpg"))
        city = City.objects.create(name='Бишкек',
                                   region=region,
                                   location=location)
        CityImage.objects.create(city_id=city, image=ContentFile(b"../../media/countries/foo.jpg"))
        accommodation = Accommodation.objects.create(name='Sheraton',
                                                     description='text',
                                                     address='Манаса 27/1',
                                                     city=city,
                                                     location=location)
        accommodation1 = Accommodation.objects.create(name='Novotel',
                                                      description='text1',
                                                      address='Манаса 27/3',
                                                      city=city,
                                                      location=location)
        AccommodationRating.objects.create(target_content_type=accommodation,
                                           rating_value=5,
                                           total_ratings=1)
        AccommodationRating.objects.create(target_content_type=accommodation,
                                           rating_value=4,
                                           total_ratings=2)
        AccommodationRating.objects.create(target_content_type=accommodation1,
                                           rating_value=5,
                                           total_ratings=1)
        AccommodationRating.objects.create(target_content_type=accommodation1,
                                           rating_value=3,
                                           total_ratings=2)

    def test_tour_get(self):
        url = reverse('tour')
        data = [{
            "name": "Novotel",
            "description": "text1",
            "address": "Манаса 27/3",
            "city": {
                "id": 1,
                "name": "Бишкек"
            },
            "location": {
                "id": 1,
                "name": "Бишкек"
            },
            "rating": 4.0
        },
            {
                "name": "Sheraton",
                "description": "text",
                "address": "Манаса 27/1",
                "city": {
                    "id": 1,
                    "name": "Бишкек"
                },
                "location": {
                    "id": 1,
                    "name": "Бишкек"
                },
                "rating": 4.5
            },
        ]
        response = self.client.get(url, format='multipart')
        stmt = Accommodation.objects.select_related('city').select_related('location').order_by('-id')
        serialized_data = AccommodationSerializer(stmt, many=True)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), data)
        unittest.mock.magic_methods()
        self.assertEquals(response.data, serialized_data.data)
