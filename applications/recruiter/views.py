from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from applications.accounts.models import User, Profile
from applications.accounts.serializers.user_serializer import CustomUserSerializer
from applications.recruiter.serializers.recruiter_serializers import RecruiterProfileUpdateSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


class RecruiterUpdateApiView(ModelViewSet):
    
    # Specify the serializer class to handle the update
    serializer_class = RecruiterProfileUpdateSerializer

    # Specify the permission classes for this view
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        try:
            # Fetch the current user instance based on the request.
            instance = self.request.user
        
            # Serialize the update request parameters using the specified serializer
            serializer = self.get_serializer(instance, data=request.data, partial=True)

            # Validate the update request parameters. If validation fails, raise an exception.
            serializer.is_valid(raise_exception=True)

            # Save the update request parameters to the database
            serializer.save()

            # Return a Response with a success message and the serialized data of the updated instance
            return Response({"message": "Updated instance", "data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle exceptions here and return an appropriate response
            error_message = str(e)
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)
        
    def get_queryset(self):
        # Return the queryset containing only the current user's instance
        return User.objects.filter(pk=self.request.user.pk)
    
    def retrieve(self, request, *args, **kwargs):
        serializer = RecruiterProfileUpdateSerializer(self.request.user)
        return Response(serializer.data)