from rest_framework.serializers import ModelSerializer
from applications.accounts.models import User, Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"