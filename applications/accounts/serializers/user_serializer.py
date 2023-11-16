from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework  import serializers
from applications.accounts.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')
        extra_kwargs = {'password': {"write_only":True}}

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email required")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already taken")
        return value
    
    def validate(self, data):
        role = data.get('role', None)
        if not role:
            raise serializers.ValidationError("Role is required")
        return data
    
