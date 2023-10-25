from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.schemas.tour import AccommodationSchema, CitySchema
from .apis import AccommodationSerializer, GetCitySerializer
from .services import AccommodationService, CityService


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
