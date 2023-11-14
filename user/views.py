from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


class RegisterUserApiView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        return Response({"status": "working"})
