from courses.models import Course
from rest_framework import serializers 


class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=5)
    number = serializers.CharField(max_length=4)
    room = serializers.CharField(max_length=4)

    def create(self,validated_data):
        return Course.objects.create(**validated_data)
    # courses = serializers.ManyToManyField(Course)