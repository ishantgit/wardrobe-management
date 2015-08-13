from django.db import models
from wardrobe.models import Wardrobe

# Create your models here.
class Item(models.Model):
	photo = models.ImageField(upload_to = 'uploads/',blank = True)
	color = models.CharField(max_length = 20)
	created_on = models.DateTimeField(auto_now_add = True)
	wardrobe = models.ManyToManyField(Wardrobe)
