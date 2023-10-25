from django.urls import path
from .views import HotelAPIView, CityAPIView

urlpatterns = [
    path(r'tour', HotelAPIView.as_view(), name='tour'),
    path(r'city', CityAPIView.as_view(), name='city'),
]
