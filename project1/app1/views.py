from rest_framework.views import  APIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated




class EmployeeAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        Employees = Employee.objects.all()
        serializer = EmployeeSerializer(Employees,many=True)
        return Response(data=serializer.data)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


class EmployeeDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,pk=None):
        obj = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(obj)
        return Response(data=serializer.data)

    def delete(self,request,pk=None):
        obj = get_object_or_404(Employee,pk=pk)
        obj.delete()
        return Response(data=None)


    def put(self,request,pk=None):
        obj = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


    def patch(self,request,pk=None):
        obj = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(data=request.data,instance=obj,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)












