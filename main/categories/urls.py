from django.urls import path

from .views import CategoryAPIView

urlpatterns = [
    path(r'category', CategoryAPIView.as_view(), name='category'),
]