from django.urls import path
from student.views import all_date

urlpatterns = [
  path("",all_date),
]