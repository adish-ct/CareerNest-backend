from rest_framework.serializers import Serializer, ModelSerializer
from ..models import Experience

class ExpenceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
    
