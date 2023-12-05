from django.shortcuts import render
from .models import Experience
from rest_framework.viewsets import ModelViewSet
from .serializers.experience_serializer import ExpenceSerializer
from rest_framework.permissions import IsAuthenticated


class ExperienceApiView(ModelViewSet):
    serializer_class = ExpenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user)
    
    



    
