from django.db.models import Avg
from rest_framework import serializers

from categories.models import Visa, Health, Gear, Includes, Excludes
from .models import Accommodation, City, Location, AccommodationRating, Region, CityImage, Destination, Tour, TypeOfTour


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


class TypeOfTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfTour
        fields = "__all__"


class VisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visa
        fields = "__all__"


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = "__all__"


class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = "__all__"


class IncludesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Includes
        fields = "__all__"


class ExcludesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excludes
        fields = "__all__"


class TourSerializer(serializers.ModelSerializer):
    destinations = DestinationsSerializer(many=True)
    type_of = TypeOfTourSerializer(many=True)
    visa_information = VisaSerializer(many=True)
    health_information = HealthSerializer(many=True)
    includes = IncludesSerializer(many=True)
    excludes = ExcludesSerializer(many=True)

    class Meta:
        model = Tour
        fields = "__all__"
