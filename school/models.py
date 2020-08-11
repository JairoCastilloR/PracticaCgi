from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    age = models.IntegerField()
    curses_student = models.CharField(max_length = 20)
    #notes

class Teacher(models.Model):
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    dni = models.IntegerField()
    curse_teacher = models.CharField(max_length = 20)

class Classroom(models.Model):
    name_number = models.IntegerField()
    capacity = models.IntegerField()
    #ubication

class Curses(models.Model):
    name_curse = models.CharField(max_length = 20)
    #Students = arreglo?

