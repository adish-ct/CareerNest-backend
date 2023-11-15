from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets




class RegisterUserApiView(APIView):
    def get(self, request):
        return Response({"message": "success"})        
    

class UserRegistrationView(viewsets.GenericViewSet):
    pass
