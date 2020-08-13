from django.urls import path
from .views import (
      StudentListView,  
      StudentDetailView,
      StudentUpdateView,
      StudentCreateView,
      StudentDeleteView,
      )
app_name = 'student'
urlpatterns = [
        path('',StudentListView.as_view(), name = 'student-list'),
        path('<int:pk>',StudentDetailView.as_view(), name = 'student-detail')  , 
        path('<int:pk>/update/',StudentUpdateView.as_view(), name = 'student-update'),
        path('create/',StudentCreateView, name = 'student-create'),
        path('<int:pk>/delete/',StudentDeleteView.as_view(), name = 'student-delete'),
        ]

