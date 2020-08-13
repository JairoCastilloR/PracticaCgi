from django.urls import path
from .views import (
        CoursesListView,
        CoursesDetailView,
        CoursesUpdateView,
        CoursesDeleteView,
        )
app_name = 'course'
urlpatterns = [
        path('',CoursesListView.as_view(), name = 'course-list'),
        path('/<int:pk>',CoursesDetailView.as_view(), name = 'course-detail'),
        path('/<int:pk>/update/',CoursesUpdateView.as_view(), name = 'course-update'),
        path('/<int:pk>/delete/',CoursesDeleteView.as_view(), name = 'course-delete'),
        ]
