from rest_framework.serializers import ModelSerializer
from applications.accounts.models import User, Profile
from applications.accounts.serializers.user_serializer import CustomUserSerializer


class RecruiterProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'about', 'address', 'place', 'city', 'state', 'zip_code', 'profile_image', 
            'banner_image', 'organization', 'employer_description', 'employer_avarage_salary', 
            'employer_head_quarters', 'user'
        ]
        extra_kwargs = {
            'user': {"read_only": True},
        }


class RecruiterProfileUpdateSerializer(ModelSerializer):
    profile = RecruiterProfileSerializer()

    class Meta:
        model = User
        fields = [
            'email', 'phone', 'role', 'username', 'is_approved', 'is_active', 'first_name', 'last_name',
            'is_staff', 'profile'
        ]

    def update(self, instance, validated_data):
        # Extract the profile information from the validated data
        profile_data = validated_data.pop('profile', None)

        # Update the user instance
        instance = super().update(instance, validated_data)

        # Update the profile instance if profile data is provided
        if profile_data:
            # profile serialization
            profile_serializer = RecruiterProfileSerializer(instance.profile, data=profile_data)

            # Update the profile instance if profil serializer is validated.
            if profile_serializer.is_valid():
                profile_serializer.save()

        return instance

       

