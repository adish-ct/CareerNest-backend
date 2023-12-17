from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from applications.accounts.models import User
from applications.jobs.models import Jobs
from applications.accounts.serializers.user_serializer import UserSerializer
from applications.jobs.serializers.job_serilizers import JobSerializer
from ..models import Application


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'user', 'job', 'status', 'is_pending', 'is_accept', 'is_reject']


class EmployerApplicationSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Application
        fields = ['id', 'user', 'job', 'status', 'is_pending', 'is_accept', 'is_reject']
        extra_kwargs = {
            'user': {'read_only': True}
        }
