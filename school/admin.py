from django.contrib import admin
from course.models import Courses
from teacher.models import Teacher
from .models import (
        Student,
        Classroom,
        )
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Courses)
