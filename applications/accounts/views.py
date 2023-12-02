from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from applications.accounts.models import User, Role, Profile
from applications.accounts.serializers.user_serializer import UserSerializer, MyTokenObtainPairSerializer
from applications.accounts.serializers.role_serializer import RoleSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from applications.accounts.serializers.profile_serializer import ProfileSerializer
from rest_framework.permissions import IsAuthenticated



class RoleApiView(viewsets.GenericViewSet):
    queryset = Role.objects.all()

    serializer_class = RoleSerializer

    def list(self, request):
        roles = self.get_queryset()
        serializer = self.get_serializer(roles, many=True)
        return Response(serializer.data)
    
class UserAPIView(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer

    # using retrive method we have to override get_query() method
    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = serializer.save()
        # creating an object of profile for the user
        Profile.objects.create(user=user)
        

    # retrive method should use pk for retrieve a specific user rather than using id.
    def retrieve(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data)
        return Response(serializer.data)


class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProfileApiView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # returning authenticated user's profile object
        return Profile.objects.filter(user=self.request.user)
    


