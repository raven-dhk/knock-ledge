from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'core/main.html')

def school(request):
    return render(request, 'core/school.html')

def teaching(request):
    return render(request, 'core/teaching.html')

def ca(request):
    return render(request, 'core/ca.html')