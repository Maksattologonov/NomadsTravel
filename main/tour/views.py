from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.schemas.tour import AccommodationSchema, CitySchema, DestinationSchema, TourSchema
from .apis import AccommodationSerializer, GetCitySerializer, DestinationsSerializer, DestinationsTitleSerializer, \
    TourSerializer
from .services import AccommodationService, CityService, DestinationService, TourService


class HotelAPIView(APIView):
    permission_classes = [AllowAny]
    schema = AccommodationSchema()

    def get(self, request, *args, **kwargs):
        if request.GET.get('id'):
            queryset = AccommodationService.get(pk=request.GET.get('id'))
        elif request.GET.get('name'):
            queryset = AccommodationService.get(name=request.GET.get('name'))
        else:
            queryset = AccommodationService.get()
        serializer = AccommodationSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CityAPIView(APIView):
    permission_classes = [AllowAny]
    schema = CitySchema()

    def get(self, request):
        if request.GET.get('id'):
            queryset = CityService.get(pk=request.GET.get('id'))
        elif request.GET.get('name'):
            queryset = CityService.get(name=request.GET.get('name'))
        else:
            queryset = CityService.get()
        serializer = GetCitySerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DestinationsAPIView(APIView):
    permission_classes = [AllowAny]
    schema = DestinationSchema()

    def get(self, request):
        if request.GET.get('title'):
            queryset = DestinationService.get(title=request.GET.get('title'))
        elif self.request.GET.get('category'):
            queryset = DestinationService.get(category=self.request.GET.get('category'))
        else:
            queryset = DestinationService.get()
        serializer = DestinationsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DestinationsTitleAPIView(APIView):
    permission_classes = [AllowAny]
    schema = DestinationSchema()

    def get(self, request):
        queryset = DestinationService.get_title()
        serializer = DestinationsTitleSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ToursAPIView(APIView):
    permission_classes = [AllowAny]
    schema = TourSchema()

    def get(self, request):
        queryset = TourService.get()
        serializer = TourSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
