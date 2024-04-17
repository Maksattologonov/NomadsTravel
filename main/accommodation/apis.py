from rest_framework import serializers

from accommodation.models import Accommodation


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = '__all__'
