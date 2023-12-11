from rest_framework.serializers import ModelSerializer
from rest_framework  import serializers
from applications.accounts.models import User, Role
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .profile_serializer import ProfileSerializer


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'profile')
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
    
    def create(self, validated_data):
        # Extract the password from the validated data
        password = validated_data.pop('password', None)

        # Create the user object without saving it to the database
        user = User(**validated_data)

        # Set the password and save the user object
        user.set_password(password)
        user.save()

        return user
    

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'role', 'username', 'is_approved', 'is_active', 'first_name', 'last_name', 'is_staff']
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        # providing user role into token for checking user is candidate or not.
        token['role'] = None
        if user.role:
            try:
                role_data = Role.objects.get(role=user.role)
                token['role'] = role_data.role
            except Exception as e:
                print(e)
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser

        return token
