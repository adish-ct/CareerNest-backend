from rest_framework.serializers import Serializer, ModelSerializer
from applications.accounts.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {"write_only":True}}