from rest_framework.serializers import Serializer, ModelSerializer
from applications.accounts.models import Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'