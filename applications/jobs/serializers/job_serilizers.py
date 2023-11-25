from rest_framework.serializers import Serializer, ModelSerializer
from ..models import Jobs
from rest_framework import serializers

class JobSerializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
    def create(self, validated_data):
        print("-----------------------")
        print(validated_data)
        print("-----------------------")
        return super().create(validated_data)