from django.urls import path
from .views import EmployeeDetails

urlpatterns = [
    path('emp/', EmployeeDetails.as_view(),name="emp"),
    path('emp/<int:id>', EmployeeDetails.as_view(), name="peremp"),
]