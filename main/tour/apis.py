from django.db.models import Avg
from rest_framework import serializers

from accommodation.models import Accommodation, AccommodationRating
from categories.models import Visa, Health, Gear, Includes, Excludes
from common.utils import avg
from .models import City, Location, Region, CityImage, Destination, Tour, \
    TypeOfTour, DestinationRating, TourDay, TourRating, Activity, DestinationImages


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


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


class LocationLatLonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('lat', 'lon')


class AccommodationSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    location = LocationSerializer()

    class Meta:
        model = Accommodation
        fields = '__all__'

    def get_rating(self, instance):
        try:
            total_ratings = AccommodationRating.objects.filter(
                target_content_type=instance.id
            ).values('rating_value').aggregate(avg_rating=Avg('rating_value'))['avg_rating']

            return total_ratings if total_ratings is not None else 0
        except Exception as e:
            return 0


class DestinationForTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'


class GetCitySerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    region = RegionSerializer()

    # images = CityImagesSerializer()

    class Meta:
        model = City
        fields = ('id', 'name', 'region', 'location',)


class DestinationRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationRating
        fields = ('value',)


class DestinationIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('pk',)


class DestinationRatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationRating
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()
    tour_id = serializers.SerializerMethodField()
    activity = serializers.SerializerMethodField()

    class Meta:
        model = Destination
        fields = ('title', 'description', 'main_image', 'coordinates', 'activity', 'tour_id')

    def get_coordinates(self, obj):
        return [obj.location.lat, obj.location.lon]

    def get_tour(self, obj):
        return [tour.title for tour in obj.tour.filter()]

    def get_activity(self, obj):
        return [activity.name for activity in obj.activity.filter()]

    def get_tour_id(self, obj):
        return [tour.title for tour in obj.tour_id.filter()]

class DestinationsSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    region = serializers.StringRelatedField(many=False)

    class Meta:
        model = Destination
        fields = ('id', 'title', 'main_image', 'ratings', 'active', 'coordinates', 'region')

    def get_coordinates(self, obj):
        return [obj.location.lat, obj.location.lon]

    def get_ratings(self, obj):
        ratings = DestinationRating.objects.filter(destination_id=obj)
        if ratings:
            total_rating = sum([rating.value for rating in ratings])
            average_rating = total_rating / len(ratings)
            return "{:.2f}".format(average_rating)
        else:
            return "0.00"


class DestinationImagesSerializer(serializers.ModelSerializer):
    alt = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = DestinationImages
        fields = ['alt', 'url']

    def get_alt(self, obj):
        return obj.image.name

    def get_url(self, obj):
        return obj.image.url


class DestinationsTitleSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()
    images = DestinationImagesSerializer(many=True, read_only=True, source='destination_image')

    class Meta:
        model = Destination
        fields = ['id', 'title', 'description', 'coordinates', 'images']

    def get_coordinates(self, obj):
        return [obj.location.lat, obj.location.lon]



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


class TourDaySerializer(serializers.ModelSerializer):
    accommodation = AccommodationSerializer(many=True, read_only=True)
    class Meta:
        model = TourDay
        fields = '__all__'
        depth = 2




class TourRatingSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    tour_name = serializers.CharField(source='tour_id.name', read_only=True)

    class Meta:
        model = TourRating
        fields = ['id', 'tour_id', 'tour_name', 'rating', 'user', 'user_name']


class TourSerializer(serializers.ModelSerializer):
    countries = serializers.SerializerMethodField()
    tour_types = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = [
            "id",
            "name",
            "description",
            "price",
            "promotion",
            "duration",
            "difficulty",
            "countries",
            "tour_types",
            "reviews",
        ]

    def get_countries(self, obj):
        return [countries.name for countries in obj.countries.all()]

    def get_tour_types(self, obj):
        return [tour_type.type for tour_type in obj.tour_types.all()]

    def get_reviews(self, obj):
        ratings = TourRating.objects.filter(tour_id=obj.id).values_list('rating', flat=True)
        if ratings.exists():
            return {
                "count": ratings.count(),
                "rating": avg(list(ratings))
            }
        return {
            "count": 0,
            "rating": None
        }

class TourDetailSerializer(serializers.ModelSerializer):
    countries = serializers.SerializerMethodField()
    tour_types = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    days = TourDaySerializer(many=True,  read_only=True)
    class Meta:
        model = Tour
        depth = 3
        fields = [
            "id",
            "name",
            "description",
            "price",
            "promotion",
            "duration",
            "difficulty",
            "countries",
            "tour_types",
            "reviews",
            "days",
        ]

    def get_countries(self, obj):
        return [countries.name for countries in obj.countries.all()]

    def get_tour_types(self, obj):
        return [tour_type.type for tour_type in obj.tour_types.all()]

    def get_reviews(self, obj):
        ratings = TourRating.objects.filter(tour_id=obj.id).values_list('rating', flat=True)
        if ratings.exists():
            return {
                "count": ratings.count(),
                "rating": avg(list(ratings))
            }
        return {
            "count": 0,
            "rating": None
        }
