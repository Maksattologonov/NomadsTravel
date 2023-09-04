from rest_framework import serializers
from .models import Accommodation, City, Location, AccommodationRating


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AccommodationSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    # city = serializers.CharField()
    # location = serializers.CharField()

    class Meta:
        model = Accommodation
        fields = ('name', 'description', 'address', 'city', 'location', 'rating')

    def get_rating(self, instance):
        print(instance)
        return AccommodationRating.objects.get(pk=instance.pk)
