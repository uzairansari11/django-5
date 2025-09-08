from django.shortcuts import render

# Create your views here.

def all_date(req):
  return render(req , "student/index.html")