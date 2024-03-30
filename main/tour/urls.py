from django.urls import path
from .views import HotelAPIView, CityAPIView, DestinationsAPIView, DestinationsTitleAPIView, ToursAPIView

urlpatterns = [
    path(r'hotels', HotelAPIView.as_view(), name='tour'),
    path(r'city', CityAPIView.as_view(), name='city'),
    path(r'destination', DestinationsAPIView.as_view(), name='destination'),
    path(r'destination/title', DestinationsTitleAPIView.as_view(), name='destination-title'),
    path(r'tour', ToursAPIView.as_view(), name='tour'),
]
