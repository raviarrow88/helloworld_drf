from django.shortcuts import render ,get_object_or_404
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serailizer import EmployeeSerializer


class EmployeeViewList(APIView):
    def display(self):
        data = '<html><body><h1>Hello, world</h1></body></html>'
        return Response({'message': data})
