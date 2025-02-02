from .models import HotelEmployee

class HotelEmployeeService:
    @staticmethod
    def create_hotel_employee(data):
        """
        Создание нового сотрудника отеля.
        """
        employee = HotelEmployee.objects.create(**data)
        return employee

    @staticmethod
    def update_hotel_employee(employee_id, data):
        """
        Обновление данных сотрудника отеля.
        """
        employee = HotelEmployee.objects.get(id=employee_id)
        for key, value in data.items():
            setattr(employee, key, value)
        employee.save()
        return employee

    @staticmethod
    def delete_hotel_employee(employee_id):
        """
        Удаление сотрудника отеля.
        """
        employee = HotelEmployee.objects.get(id=employee_id)
        employee.delete()