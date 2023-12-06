from typing import Any
from rest_framework.serializers import Serializer, ModelSerializer
from ..models import Experience
from django.core.exceptions import ValidationError
from django.utils import timezone


class CustomFieldValidator:
    def __call__(self, value):
        if not value.replace(" ", "").isalpha():
            raise ValidationError("Should contain alphabets only")


class CustomDateValidator:
    
    def __call__(self, date ):
        if date and date > timezone.now().date():
            raise ValidationError("Invalid date input")
    

class ExpenceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        extra_kwargs = {
            'job_role': {'validators': [CustomFieldValidator()],},
            'organization': {'validators': [CustomFieldValidator()],},
            'location': {'validators': [CustomFieldValidator()],},
            'start_date': {'validators': [CustomDateValidator()],},
            'end_date': {'validators': [CustomDateValidator()],},
        }
    
