from rest_framework.serializers import ModelSerializer
from ..models import Profile


class ProfileSerializer(ModelSerializer): 
    class Meta:
        model = Profile
        fields = '__all__'
        # extra_kwargs = {'user':{'read_only': True}}
