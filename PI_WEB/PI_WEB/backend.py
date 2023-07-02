from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from PI_WEB.models import Servidor
class ServidorBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        try:
            servidor = Servidor.objects.get(pk=kwargs['ra'])
            if kwargs['password'] == servidor.password:
                print("senha certa")
                return servidor
        except:
            pass
        return None

    def get_user(self, user_id):
        user_id = '00' + str(user_id)
        return Servidor.objects.get(pk=user_id)

    def has_perm(self, user_obj, perm):
        return True