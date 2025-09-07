from django.urls import path
from demo.views import learnDjango,myFn
urlpatterns = [
  path("py/",learnDjango),
  path("my/",myFn)
]