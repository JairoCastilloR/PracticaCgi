from django.contrib import admin
from .models import (
        Student,
        Teacher,
        Classroom,
        Courses,
        )
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Courses)
