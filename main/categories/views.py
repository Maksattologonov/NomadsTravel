from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.apis import CategorySerializer
from categories.services import CategoryService


class CategoryAPIView(APIView):
    def get(self, request):
        queryset = CategoryService.get_categories()
        serializer = CategorySerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
