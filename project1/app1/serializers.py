from rest_framework import  serializers
from .models import Employee




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'



    def create(self, validated_data):
        return Employee.objects.create(**validated_data)



    def update(self, instance, validated_data):
        instance.eid=validated_data.get("eid",instance.eid)
        instance.name=validated_data.get("name",instance.name)
        instance.sal=validated_data.get("sal",instance.sal)
        instance.age=validated_data.get("age",instance.age)
        instance.save()
        return instance