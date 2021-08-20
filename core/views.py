from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'core/main.html')

def school(request):
    return HttpResponse('school')

def message(request):
    return HttpResponse('message')