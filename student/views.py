from django.shortcuts import render
from student.models import Profile

# Create your views here.


def all_date(req):
    students_data = Profile.objects.all()
    single_student_data = Profile.objects.get(pk=1)
    print(
        f" this is student data {students_data} || single student data {single_student_data}")
    return render(req, "student/index.html", {"student_data": students_data})
