from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers.experience_serializer import ExpenceSerializer
from .serializers.education_serializer import EducationSerializer
from .models import Experience, Education

class ExperienceApiView(ModelViewSet):
    serializer_class = ExpenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user)
    

class EducationApiView(ModelViewSet):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Education.objects.filter(user=self.request.user)
    