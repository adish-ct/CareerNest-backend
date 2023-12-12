from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers.application_serializer import ApplicationSerializer
from .models import Application
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.tokens import AccessToken

class IsEmployerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role

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
            return Application.objects.filter(job_id=job_id).select_related('user__profile')
        
    
    def update(self, request, *args, **kwargs):
        
        auth_header = self.request.META.get('HTTP_AUTHORIZATION', '').split('Bearer ')
        if len(auth_header) != 2:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        jwt_token = auth_header[1]

        try:
            decoded_token = AccessToken(jwt_token)
            role = decoded_token.payload.get('role')
            if role != 'Employer':
                return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

# need to override get_object() method
        partial = kwargs.pop('partial', True)
        instance = Application.objects.get(id=self.kwargs.get('pk'))
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)