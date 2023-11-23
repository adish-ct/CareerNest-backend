from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from applications.accounts.models import User, Role
from applications.accounts.serializers.user_serializer import UserSerializer
from applications.accounts.serializers.role_serializer import RoleSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from applications.accounts.serializers.user_serializer import MyTokenObtainPairSerializer



class RoleApiView(APIView):
    def get(self, request):
        return Response({"msg": "view working"})


