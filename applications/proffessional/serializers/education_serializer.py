from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from ..models import Education
from django.core.exceptions import ValidationError



class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("Start date must be less than end date")
        return data