from PortalUV.apps.alumnos.models import Alumno
from django.contrib.auth.models import User, check_password

class UvAuth(object):
 
    
    def authenticate(self, username=None, password=None):
        try:
            user = Alumno.objects.get(matricula=username)
            if user.check_password(password):
                return user
        except Alumno.DoesNotExist:
            return None 

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return Alumno.objects.get(matricula=user_id)
        except Alumno.DoesNotExist:
            return None