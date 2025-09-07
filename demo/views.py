from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def myFn(request):
    return HttpResponse("Hello this is my first api")


def learnDjango(request, **kwargs):
    values = {"course_name": "Django 5.1"}
    return render(request, 'demo/index.html', context=values)
