from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=5, null=False, blank=False)
    number = models.CharField(max_length=4, null=False, blank=False)
    room = models.CharField(max_length=4, default='')