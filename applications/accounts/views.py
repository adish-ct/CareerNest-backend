from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from applications.accounts.models import User, Role
from applications.accounts.serializers.user_serializer import UserSerializer
from applications.accounts.serializers.role_serializer import RoleSerializer
from rest_framework import status


class RoleApiView(viewsets.GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def list(self, request):
        roles = self.get_queryset()
        serializer = self.get_serializer(roles, many=True)
        return Response(serializer.data)
    
class UserRegisterAPIView(CreateModelMixin, viewsets.GenericViewSet):
    user = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        role = request.data.get('role')
        print(role)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # perform_handled customize the behaviour when an object created. if we want to perform any additional operations
    def perform_create(self, serializer):
        serializer.save()


