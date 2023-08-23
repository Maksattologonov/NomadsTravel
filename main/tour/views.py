from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .apis import HotelSerializer
from .services import HotelService


class HotelAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = HotelService.get()
        serializer = HotelSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
