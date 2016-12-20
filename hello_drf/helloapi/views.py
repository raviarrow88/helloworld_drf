from django.shortcuts import render ,get_object_or_404
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serailizer import EmployeeSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .pagination import EmployeeLimitPagination
from rest_framework import serializers
#from rest_framework.generics import ListAPIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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