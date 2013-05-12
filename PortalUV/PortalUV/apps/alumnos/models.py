from django.contrib.auth.models import User
from django.db import models

class Alumno(User):
	matricula = models.CharField(max_length=10,primary_key=True)
	
	def __unicode__(self):
		return self.matricula