from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Deltager(User):

	antall_trekkninger=models.IntegerField(blank=True)
	
	def __str__(self):
		return f'Logget inn som @{username}'

