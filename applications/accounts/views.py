from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from applications.accounts.models import User
from applications.accounts.serializers.user_serializer import UserSerializer
from rest_framework import status



class RegisterUserApiView(APIView):
    def get(self, request):
        return Response({"message": "success"})        
    

class UserRegisterAPIView(CreateModelMixin, GenericViewSet):
    user = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # perform_handled customize the behaviour when an object created. if we want to perform any additional operations
    def perform_create(self, serializer):
        serializer.save()

