from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from applications.jobs.models import Jobs
from .serializers.job_serilizers import JobSerializer



class JobsApiView(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer


