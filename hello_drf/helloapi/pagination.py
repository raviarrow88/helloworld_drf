from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class EmployeeLimitPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10