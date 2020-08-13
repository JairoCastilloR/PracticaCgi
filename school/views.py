from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
        View,
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView,
        )
from .models import Student
# Create your views here.
class StudentListView(ListView):
    model = Student
class StudentDetailView(DetailView):
    model = Student
class StudentCreateView(CreateView):
    model = Student
    fields = [ 
            'name_student',
            'surname',
            'age',
            'dni',
            'user_student',
            'courses',
            'gender',
            ]
class StudentUpdateView(UpdateView):
    model = Student
    fields = [ 
            'name_student',
            'surname',
            'age',
            'dni',
            'user_student',
            'courses',
            'date_creation',
            'gender',
                ]
    template_name_suffix = '_update_form'
class StudentDeleteView(DeleteView):
    model =Student
    succes_url = reverse_lazy('course:course-list')
class StudentQueryView(View):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.filter(credits__lte = '5')
        return JsonResponse(list(queryset.values()),safe = False)
