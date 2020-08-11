from django.contrib import admin
from .models import (
        Student,
        Teacher,
        Classroom,
        Curses,
        )
# Register your models here.
admin.site.register(Student)
