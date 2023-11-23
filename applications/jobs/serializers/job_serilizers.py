from rest_framework.serializers import Serializer, ModelSerializer
from ..models import Jobs
from rest_framework import serializers

class JobSerializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'