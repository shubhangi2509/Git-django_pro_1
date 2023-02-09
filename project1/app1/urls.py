from django.urls import  path
from .views import EmployeeAPI,EmployeeDetails



urlpatterns = [
    path('emp/',EmployeeAPI.as_view()),
    path('emp/<int:pk>/',EmployeeDetails.as_view())
]