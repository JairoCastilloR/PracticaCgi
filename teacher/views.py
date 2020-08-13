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
from .models import Teacher
# Create your views here.
class TeacherListView(ListView):
    model = Teacher
class TeacherDetailView(DetailView):
    model = Teacher
class TeacherCreateView(CreateView):
    model = Teacher
    fields = [ 
            'name_teacher',
            'surname',
            'age',
            'dni',
            'courses',
            'date_creation',
            'gender',
            ]
class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = [ 
            'name_teacher',
            'surname',
            'age',
            'dni',
            'courses',
            'date_creation',
            'gender',
                ]
    template_name_suffix = '_update_form'
class TeacherDeleteView(DeleteView):
    model =Teacher
    succes_url = reverse_lazy('course:course-list')
class TeacherQueryView(View):
    def get(self, request, *args, **kwargs):
        queryset = Teacher.objects.filter(credits__lte = '5')
        return JsonResponse(list(queryset.values()),safe = False)
