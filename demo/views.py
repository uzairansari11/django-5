from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def myFn(request):
    return HttpResponse("Hello this is my first api")


def learnDjango(request, **kwargs):
    d = datetime.now()
    values = {"course_name": "Django 5.1","description":"Hey this is django templating engine default one used by django",'current_time':d}
    return render(request, 'demo/index.html', context=values)
