from alumnos.models import Alumno
from django.contrib.auth.models import check_password

class UvAuth(object):
 
    
    def authenticate(self, matricula=None, password=None):
        try:
            user = Alumno.objects.get(matricula=matricula)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None 

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return Alumno.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None