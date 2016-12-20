from django.shortcuts import render ,get_object_or_404
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serailizer import EmployeeSerializer
import json


class EmployeeViewList(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serailizer_class = EmployeeSerializer(employees,many=True)
        return Response(serailizer_class.data)
