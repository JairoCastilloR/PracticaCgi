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
from .models import Courses
# Create your views here.
class CoursesListView(ListView):
    model = Courses
class CoursesDetailView(DetailView):
    model = Courses
class CoursesCreateView(CreateView):
    model = Courses
    fields = [ 
            'name_curse',
            'capacity_curse',
            'credits',
            ]
class CoursesUpdateView(UpdateView):
    model = Courses
    fields = [ 
                'name_curse',
                'capacity_curse',
                'credits',
                ]
    template_name_suffix = '_update_form'
class CoursesDeleteView(DeleteView):
    model =Courses
    succes_url = reverse_lazy('course:course-list')
class CoursesQueryView(View):
    def get(self, request, *args, **kwargs):
        queryset = Courses.objects.filter(credits__lte = '5')
        return JsonResponse(list(queryset.values()),safe = False)

