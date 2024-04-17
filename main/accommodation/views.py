from django.shortcuts import render
from rest_framework.views import APIView


class AccommodationAPIView(APIView):
    def get(self, request):
        return render(request, 'accommodation.html')
