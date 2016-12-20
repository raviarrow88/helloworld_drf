from django.shortcuts import render ,get_object_or_404
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serailizer import EmployeeSerializer
from rest_framework import generics,status
from .pagination import EmployeeLimitPagination
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from django.http import Http404



class EmployeeViewList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeeLimitPagination
    '''
    def get(self,request):
        queryset = self.get_queryset()
        serailizer = EmployeeSerializer(queryset,many=True)
        return Response(serailizer.data)
    '''
class EmployeeGetView(APIView):
    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request,id):
        employee = self.get_object(id)
        serailizer_class = EmployeeSerializer(employee)
        return Response(serailizer_class.data)
