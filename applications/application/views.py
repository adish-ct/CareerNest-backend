from django.shortcuts import render
from .serializers.application_serializer import ApplicationSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Application

class ApplicationApiView(ModelViewSet):
    
    serializer_class = ApplicationSerializer
    def get_queryset(self):
        return Application.objects.filter(user=self.request.user, job=self.request.data['job'])
