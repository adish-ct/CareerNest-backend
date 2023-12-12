from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers.experience_serializer import ExpenceSerializer
from .serializers.education_serializer import EducationSerializer
from .serializers.project_serializer import ProjectSerializer
from .serializers.skills_serializer import SkillsSerializer
from .models import Experience, Education, Project, Skill

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
    

class SkillsApiView(ModelViewSet):
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        role = self.request.query_params.get('role')
        user_id = self.request.query_params.get('user_id')
        if role is not None and user_id is not None and role == 'Employer':
            return Skill.objects.filter(user=user_id)
        return Skill.objects.filter(user=self.request.user)