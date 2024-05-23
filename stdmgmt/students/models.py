from django.db import models
# from courses import Course


# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=20, null=False, blank=False)
    lastname = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    student_id = models.CharField(max_length=10, default='999999')
    courses = models.ManyToManyField(Course)