from django.db import models

# Create your models here.
class Student(models.Model):
    name_student = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    #age = models.IntegerField()
    #dni = models.SlugField()
    user_student = models.CharField(max_length = 20)
    courses = models.ManyToManyField('Courses')
    date_creation_student = models.DateField(auto_now = True)
    gender = models.BooleanField()
    #notes
    #image
    def __str__(self):
        return self.name_student

class Teacher(models.Model):
    name_teacher = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    age = models.IntegerField()
    dni = models.SlugField()
    courses = models.ForeignKey('Courses', on_delete = models.CASCADE)
    date_creation_teacher = models.DateField(auto_now = True)
    gender = models.BooleanField()
    #input notes
    #image
    def __str__(self):
        return self.name_teacher


class Classroom(models.Model):
    name_number = models.IntegerField()
    capacity = models.IntegerField()
    #ubication
    def __str__(self):
        return self.name_number


class Courses(models.Model):
    name_curse = models.CharField(max_length = 20)
    capacity_curse = models.SlugField()
    credits = models.IntegerField()
    #Students = arreglo?
    def __str__(self):
        return self.name_curse

