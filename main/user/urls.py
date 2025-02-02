from django.urls import path
from .views import (
    GuideListCreateAPIView, GuideRetrieveUpdateDestroyAPIView,
    HotelEmployeeListCreateAPIView, HotelEmployeeRetrieveUpdateDestroyAPIView
)

urlpatterns = [

    path('guides/', GuideListCreateAPIView.as_view()),
    path('guides/<int:pk>/', GuideRetrieveUpdateDestroyAPIView.as_view()),

    path('hotel-employees/', HotelEmployeeListCreateAPIView.as_view()),
    path('hotel-employees/<int:pk>/', HotelEmployeeRetrieveUpdateDestroyAPIView.as_view()),
]