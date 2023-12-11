from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers.application_serializer import ApplicationSerializer
from .models import Application

class ApplicationApiView(ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_queryset(self):
        user = self.request.user
        job_id = self.request.query_params.get('job')
        role = self.request.query_params.get('role')

        if job_id is not None and role == 'Candidate':
            return Application.objects.filter(user=user, job=job_id)
        else:
            applications = Application.objects.filter(job_id=job_id)
            applications = applications.select_related('user__profile')
            return applications
        
