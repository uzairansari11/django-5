from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None   # remove username field
    email = models.EmailField(unique=True)  # make email unique
    
    USERNAME_FIELD = "email"   # use email as login field
    REQUIRED_FIELDS = []       # no extra fields required
