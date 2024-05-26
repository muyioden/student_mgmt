from students.models import Student
from rest_framework import serializers 


class StudentSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=25)
    lastname = serializers.CharField(max_length=25)
    email = serializers.EmailField()
    student_id = serializers.CharField(max_length=10, default='999999')

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    # courses = serializers.ManyToManyField(Course)