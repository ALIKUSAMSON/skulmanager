from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class EmailBackEnd(ModelBackend):
    def authenticate(self,usrename=None,password=None,**kwargs):
        UserModel = User()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None