from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from .models import HotelEmployee
from .apis import HotelEmployeeSerializer
from .models import Guide
from .apis import GuideSerializer


class HotelEmployeeListCreateAPIView(APIView):
    """
    Список всех сотрудников отеля и создание нового сотрудника.
    """
    def get(self, request):
        employees = HotelEmployee.objects.all()
        serializer = HotelEmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelEmployeeRetrieveUpdateDestroyAPIView(APIView):
    """
    Получение, обновление и удаление конкретного сотрудника отеля.
    """
    def get_object(self, pk):
        try:
            return HotelEmployee.objects.get(pk=pk)
        except HotelEmployee.DoesNotExist:
            return None

    def get(self, request, pk):
        employee = self.get_object(pk)
        if employee:
            serializer = HotelEmployeeSerializer(employee)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        employee = self.get_object(pk)
        if employee:
            serializer = HotelEmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        if employee:
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)



class GuideListCreateAPIView(APIView):
    """
    Список всех гидов и создание нового гида.
    """
    def get(self, request):
        guides = Guide.objects.all()
        serializer = GuideSerializer(guides, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuideRetrieveUpdateDestroyAPIView(APIView):
    """
    Получение, обновление и удаление конкретного гида.
    """
    def get_object(self, pk):
        try:
            return Guide.objects.get(pk=pk)
        except Guide.DoesNotExist:
            return None

    def get(self, request, pk):
        guide = self.get_object(pk)
        if guide:
            serializer = GuideSerializer(guide)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        guide = self.get_object(pk)
        if guide:
            serializer = GuideSerializer(guide, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        guide = self.get_object(pk)
        if guide:
            guide.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


