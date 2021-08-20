from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('school/', views.school),
    path('message/', views.message),
]
