from models import Student
from rest_framework import serializers 


class StudentSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    student_id = serializers.CharField(max_length=10, default='999999')
    # courses = serializers.ManyToManyField(Course)
