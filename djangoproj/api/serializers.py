from rest_framework import serializers
from .models import Student,DataFrameStorage
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['stuname','email']

class optionserializer(serializers.ModelSerializer):
    class Meta:
        model = DataFrameStorage
        fields = ['data']