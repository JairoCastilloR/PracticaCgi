from django.db import models
from course.models import Courses
from django.urls import reverse
# Create your models here.
class Teacher(models.Model):

  name_teacher = models.CharField(max_length = 20)
  surname = models.CharField(max_length = 20)
  age = models.IntegerField()
  dni = models.SlugField()
  courses = models.ForeignKey(Courses, on_delete = models.CASCADE)
  date_creation_teacher = models.DateField(auto_now = True)
  STATUS = (
          ('Male', 'Male'),
          ('Female', 'Female'),
          ('another', 'Weird')
          )
  gender = models.CharField(max_length = 20, choices = STATUS,blank = True, default = 'Male')
  #input notes
  #image
  def __str__(self):
      return self.name_teacher

  def get_absolute_url (self):
      return reverse('teacher:teacher-detail', kwargs = { 'pk': self.id})



