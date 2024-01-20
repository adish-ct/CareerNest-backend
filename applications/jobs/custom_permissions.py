from rest_framework.permissions import BasePermission
from .models import Jobs
from django.shortcuts import get_object_or_404


class IsJobOwner(BasePermission):
    def has_permission(self, request, view):
        job_id = view.kwargs.get('pk')
        print("job_id:", job_id)
        job = get_object_or_404(Jobs, pk=job_id)
        print("job.employer:", job.employer)
        return job.employer == request.user
