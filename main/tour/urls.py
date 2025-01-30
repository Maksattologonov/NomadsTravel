from django.urls import path
from .views import HotelAPIView, CityAPIView, DestinationsAPIView, DestinationsTitleAPIView, DestinationRatingAPIView, \
    ToursAPIView, DestinationAPIView, ToursDetailAPIView

urlpatterns = [
    path(r'hotels', HotelAPIView.as_view(), name='tour'),
    path(r'city', CityAPIView.as_view(), name='city'),
    path(r'destinations', DestinationsAPIView.as_view(), name='destinations'),
    path(r'destination', DestinationAPIView.as_view(), name='destination'),
    # path(r'destination/title', DestinationsTitleAPIView.as_view(), name='destination-title'),
    path(r'destination/rating/create', DestinationRatingAPIView.as_view(), name='destination-rating-create'),
    path(r'tour', ToursAPIView.as_view(), name='tour'),
    path(r'tour/detail/<int:id>/', ToursDetailAPIView.as_view(), name='tour'),
]
