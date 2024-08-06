from django.db import models

# Create your models here.
class Student_table(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    contact = models.IntegerField()
    course = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    password = models.CharField(max_length=8)