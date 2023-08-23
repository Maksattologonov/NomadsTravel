from rest_framework import serializers
from .models import Accommodation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = '__all__'
