from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from applications.accounts.models import User
from applications.accounts.serializers.user_serializer import UserSerializer



class RegisterUserApiView(APIView):
    def get(self, request):
        return Response({"message": "success"})        
    

class UserRegisterAPIView(CreateModelMixin, GenericViewSet):
    user = User.objects.all()
    serializer_class = UserSerializer
