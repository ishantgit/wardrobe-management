from django.db import models
from account.models import MyUser

# Create your models here.
class Wardrobe(models.Model):
	user = models.ForeignKey(MyUser,primary_key = True)
	created_on = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.user + self.created_on
