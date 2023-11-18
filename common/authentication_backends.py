from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from applications.accounts.models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password) and user.is_active:
            return user
        
        return None