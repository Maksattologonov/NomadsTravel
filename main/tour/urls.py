from django.urls import path
from .views import HotelAPIView

urlpatterns = [
    path('tour/', HotelAPIView.as_view(), name='tour')
]
