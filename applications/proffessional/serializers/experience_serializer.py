from rest_framework.serializers import Serializer, ModelSerializer
from ..models import Experience
from django.core.exceptions import ValidationError


def CustomExperienceFieldValidator(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError('should only conatins alphabets')

class ExpenceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        extra_kwargs = {
            'job_role': {
                'validators': [CustomExperienceFieldValidator],
            },
        }
    
