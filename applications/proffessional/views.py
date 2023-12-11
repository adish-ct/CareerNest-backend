from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers.experience_serializer import ExpenceSerializer
from .serializers.education_serializer import EducationSerializer
from .serializers.project_serializer import ProjectSerializer
from .models import Experience, Education, Project

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
    

class ProjectApiView(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)