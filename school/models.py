from django.db import models
from course.models import Courses
# Create your models here.
class Student(models.Model):
    name_student = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    age = models.IntegerField()
    dni = models.SlugField()
    user_student = models.CharField(max_length = 20)
    courses = models.ManyToManyField(Courses)
    date_creation_student = models.DateField(auto_now = True)
    STATUS = (                                                                         
        ('Male', 'Male'),           
        ('Female', 'Female'),    
        ('another', 'Weird')
        )                                                                          
    gender = models.CharField(max_length = 20, choices = STATUS,blank = True, default =   'Male')
#notes
    #image
    def __str__(self):
        return self.name_student

class Classroom(models.Model):
    name_number = models.IntegerField()
    capacity = models.IntegerField()
    #ubication
    def __str__(self):
        return self.name_number


