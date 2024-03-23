from django.urls import path

from .views import EmployeeProfileView, EmployeeCreateView

urlpatterns = [
    path('employee/create/', EmployeeCreateView.as_view(), name='create_employee'),
    path('employee/<int:pk>', EmployeeProfileView.as_view(), name='employee_profile'),
]