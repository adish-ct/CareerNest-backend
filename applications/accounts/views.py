from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from applications.accounts.models import User, Role, Profile
from applications.accounts.serializers.user_serializer import UserSerializer, MyTokenObtainPairSerializer, CustomUserSerializer
from applications.accounts.serializers.role_serializer import RoleSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from applications.accounts.serializers.profile_serializer import ProfileSerializer
from rest_framework.permissions import IsAuthenticated



class RoleApiView(viewsets.GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def list(self, request):
        roles = self.get_queryset()
        serializer = self.get_serializer(roles, many=True)
        return Response(serializer.data)
    
class UserAPIView(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet, ListModelMixin):
    serializer_class = UserSerializer

    def get_queryset(self):
        role = self.request.query_params.get('role')
        if role:
            return User.objects.filter(role__role=role).order_by('id')
        return User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update':
            return CustomUserSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = serializer.save()
        # Creating an object of profile for the user
        Profile.objects.create(user=user)
        
    def retrieve(self, request, pk, *args, **kwargs):
        # Use get_object() method to retrieve the instance
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        print("------------------------------")
        print(self.request.data)
        print("------------------------------")

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProfileApiView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # returning authenticated user's profile object
        return Profile.objects.filter(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()



