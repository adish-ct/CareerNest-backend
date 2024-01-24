from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from applications.accounts.models import User, Role, Profile
from applications.accounts.serializers.user_serializer import UserSerializer, MyTokenObtainPairSerializer, \
    CustomUserSerializer
from applications.accounts.serializers.role_serializer import RoleSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from applications.accounts.serializers.profile_serializer import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
import random
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import viewsets, mixins, status
from rest_framework import generics


class RoleApiView(viewsets.GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def list(self, request):
        roles = self.get_queryset()
        serializer = self.get_serializer(roles, many=True)
        return Response(serializer.data)


class UserAPIView(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet, ListModelMixin):
    serializer_class = UserSerializer

    def get_queryset(self):
        role = self.request.query_params.get('role')
        if role:
            return User.objects.filter(role__role=role).order_by('id')
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update':
            return CustomUserSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = serializer.save()
        Profile.objects.create(user=user)

    def retrieve(self, request, pk, *args, **kwargs):
        # Use get_object() method to retrieve the instance
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


@receiver(post_save, sender=User)
def send_otp_on_user_creation(sender, instance, created, **kwargs):
    if created:
        send_otp(instance.email)


def send_otp(email):
    try:
        subject = f'Your verification email - {email}'
        otp = random.randint(100000, 999999)
        message = f'your otp is {otp}'
        email_from = 'ceetey1997@gmail.com'
        send_mail(subject, message, email_from, ['adishathu525@gmail.com'])
        user = User.objects.get(email=email)
        user.token = otp
        user.save()
    except Exception as e:
        # Handle exceptions (e.g., email sending failure or user retrieval failure)
        print(f"Error sending OTP: {e}")


class OtpValidationView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        otp = request.data.get('otp', None)

        # Validate that 'email' and 'otp' are provided in the request
        if not email or not otp:
            return Response({'error': 'Session Timeout'}, status=status.HTTP_400_BAD_REQUEST)

        # Perform OTP validation logic
        try:
            user = User.objects.get(email=email, token=otp, is_verified=False)
            # If OTP is valid, you can mark it as used or invalidate it in the database
            user.is_verified = True
            user.save()
            return Response({'valid': True}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'valid': False}, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProfileApiView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # returning authenticated user's profile object
        return Profile.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()



class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Welcome social Authentication '}
        return Response(content)
