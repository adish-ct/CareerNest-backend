from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from applications.accounts.serializers.user_serializer import UserSerializer
from ..models import Application

class ApplicationSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Application
        fields = ['user', 'job', 'status', 'is_pending', 'is_accept', 'is_reject']
        
