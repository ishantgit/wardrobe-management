from django.db import models
from account.models import MyUser

# Create your models here.
class Wardrobe(models.Model):
	user = models.ForeignKey(MyUser)
	created_on = models.DateTimeField(auto_now_add = True)


