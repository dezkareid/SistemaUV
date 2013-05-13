from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.db import models

 
class AlumnoManager(BaseUserManager):
    def create_user(self, matricula, password=None):
        if not matricula:
            raise ValueError('Users must have an email address')
 
        user = self.model(matricula=matricula)
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, matricula, password):
        user = self.create_user(matricula, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user
 

class Alumno(AbstractBaseUser):
	matricula = models.CharField(max_length=10, unique=True, db_index=True)
	is_active = models.BooleanField(default=True)
	is_admin= models.BooleanField(default=False)
 	USERNAME_FIELD = 'matricula'
 	objects = AlumnoManager()
 
 	def get_full_name(self):
		return self.matricula
 
	def get_short_name(self):
		return self.matricula
	
	def has_perm(self, perm, obj=None):
		return True
	
	def has_module_perms(self, app_label):
		return True
	
	@property
	def is_staff(self):
		return self.is_admin

	def __unicode__(self):
		return self.matricula