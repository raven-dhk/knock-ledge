from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('school/', views.school, name='school'),
    path('teaching/', views.teaching, name='teaching'),
    path('ca/', views.ca, name='ca'),
]
