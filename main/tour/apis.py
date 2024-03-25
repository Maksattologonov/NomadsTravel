from django.db.models import Avg
from rest_framework import serializers
from .models import Accommodation, City, Location, AccommodationRating, Region, CityImage, Destination


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class CityImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityImage
        fields = ('image',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')


class AccommodationSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    city = CitySerializer()
    location = LocationSerializer()

    class Meta:
        model = Accommodation
        fields = ('name', 'description', 'address', 'city', 'location', 'rating')

    def get_rating(self, instance):
        try:
            total_ratings = AccommodationRating.objects.filter(
                target_content_type=instance.id
            ).values('rating_value').aggregate(avg_rating=Avg('rating_value'))['avg_rating']

            return total_ratings if total_ratings is not None else 0
        except Exception as e:
            return 0


class GetCitySerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    region = RegionSerializer()
    # images = CityImagesSerializer()

    class Meta:
        model = City
        fields = ('id', 'name', 'region', 'location',)


class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'


class DestinationsTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('title', 'main_image')

