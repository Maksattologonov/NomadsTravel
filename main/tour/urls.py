from django.urls import path
from .views import get_hi

urlpatterns = [
    path('tour/', get_hi)
]