from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
	GENDER_CHOICES = (('M','Male'),('F','Female'),)
	gender = models.CharField(max_length=1, choices = GENDER_CHOICES ,default = GENDER_CHOICES[0][0])
