from msilib.schema import ListView

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from common.schemas.tour import AccommodationSchema, CitySchema, DestinationSchema, TourSchema, DestinationRatingSchema, \
    DestinationsSchema
from .apis import AccommodationSerializer, GetCitySerializer, DestinationsSerializer, DestinationsTitleSerializer, \
    TourSerializer, DestinationRatingSerializer, DestinationRatingCreateSerializer, DestinationSerializer
from .models import Tour
from .services import AccommodationService, CityService, DestinationService, TourService, DestinationRouteService


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
    schema = DestinationsSchema()

    def get(self, request):
        if request.GET.get('title'):
            queryset = DestinationService.filter(title=request.GET.get('title'))
        elif self.request.GET.get('category'):
            queryset = DestinationService.filter(category=self.request.GET.get('category'))
        else:
            queryset = DestinationService.filter()
        serializer = DestinationsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DestinationAPIView(APIView):
    permission_classes = [AllowAny]
    schema = DestinationSchema()

    def get(self, request):
        if request.query_params.get('id'):
            queryset = DestinationService.get(id=request.query_params.get('id'))
        else:
            queryset = DestinationService.get(id=1)
        print(queryset)
        serializer = DestinationSerializer(queryset, many=True)
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
    model = Tour

    def get(self, request):
        queryset = TourService.get(request)
        serializer = TourSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    # def get(self, request):
    #     queryset = TourService.get()
    #     serializer = TourSerializer(queryset, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)


class DestinationRatingAPIView(APIView):
    permission_classes = [AllowAny]
    schema = DestinationRatingSchema()

    def post(self, request):
        serializer = DestinationRatingCreateSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print(serializer.validated_data)
            DestinationRouteService.save_rating(pk=serializer.validated_data.get('destination'),
                                                value=serializer.validated_data.get('value'))
            return Response("Destination Rating Created", status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


