from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from applications.jobs.models import Jobs
from .serializers.job_serilizers import JobSerializer
from rest_framework.permissions import IsAuthenticated
from .custom_permissions import IsJobOwner


class JobsApiView(viewsets.ModelViewSet):
    queryset = Jobs.objects.filter(employer__is_active=True)
    serializer_class = JobSerializer


class EmployerJobsApiView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            employer_id = self.request.user.id
            queryset = Jobs.objects.filter(employer=employer_id)
            return queryset
        except Exception as e:
            return Response({"error": "Internal Server Error"}, status=500)


