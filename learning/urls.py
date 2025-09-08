"""
URL configuration for learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from demo.views import myFn, learnDjango
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("demo.urls")),
    path("student/", include("student.urls"))


]


# This handles not found routes | DEBUG = False ALLOWED_HOSTS=["*"] | Otherwise will not work
def route_not_found(request, exception=None):
    return JsonResponse({"message": "This route doesn't exist"}, status=404)


handler404 = route_not_found
