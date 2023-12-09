from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import Project
from ..validators.custom_validators import CustomDateValidator

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'start_date': {'validators': [CustomDateValidator()],},
            'end_date': {'validators': [CustomDateValidator()],}
        }
        
    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("Start date must be less than end date")
        return data

