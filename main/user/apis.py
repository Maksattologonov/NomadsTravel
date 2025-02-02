from rest_framework import serializers
from .models import Guide, HotelEmployee, OtherEmployee


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'

class HotelEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelEmployee
        fields = '__all__'

class OtherEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherEmployee
        fields = '__all__'


