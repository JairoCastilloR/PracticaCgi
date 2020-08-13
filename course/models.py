from django.db import models
from django.urls import reverse
# Create your models here.
class Courses(models.Model):
  name_curse = models.CharField(max_length = 20)
  capacity_curse = models.SlugField()
  credits = models.IntegerField()
  #Students = arreglo?
  def __str__(self):
      return self.name_curse                                                       

  def get_absolute_url (self):
        return reverse('course:course-detail', kwargs = { 'pk': self.id})


