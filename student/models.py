from django.db import models
# Create your models here.

class Profile ( models.Model):
  name = models.CharField(max_length=70)
  email = models.EmailField(max_length=255)
  city = models.CharField(max_length=70)
  roll_number = models.IntegerField()
  state=models.CharField(max_length=70)
  comment = models.CharField(max_length=70,default="nothing")


""" 
Table naming convention ===> app_name + model_name |  student_profile

python manage.py makemigrations

python manage.py migrate

python manage.py showmigrations

python manage.py sqlmigrate app_name migration_file_name

"""