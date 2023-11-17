from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from applications.accounts.models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = User.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        
        return None  # Add this line to handle the case when the password does not match

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:  
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None