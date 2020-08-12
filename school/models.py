from django.db import models

# Create your models here.
class Student(models.Model):
    name_student = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    age = models.IntegerField()
    dni = models.SlugField()
    gender = models.BooleanField()
    user_student = models.CharField(max_length = 20)
    curses = models.ForeignKey('Curses', on_delete = models.CASCADE)
    #notes
    #image
    def __str__(self):
        return self.name_student

class Teacher(models.Model):
    name_teacher = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    age = models.IntegerField()
    dni = models.SlugField()
    gender = models.BooleanField()
    #input notes
    #image
    curses = models.ForeignKey('Curses', on_delete = models.CASCADE)
    def __str__(self):
        return self.name_teacher


class Classroom(models.Model):
    name_number = models.IntegerField()
    capacity = models.IntegerField()
    #ubication
    def __str__(self):
        return self.name_number


class Curses(models.Model):
    name_curse = models.CharField(max_length = 20)
    capacity_curse = models.IntegerField()
    credits = models.IntegerField()
    #Students = arreglo?
    def __str__(self):
        return self.name_curse

