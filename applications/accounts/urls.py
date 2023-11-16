from rest_framework import routers
from django.urls import path
from applications.accounts.views import RegisterUserApiView, UserRegisterAPIView

urlpatterns = [
    path('', RegisterUserApiView.as_view()),
    path('register/', UserRegisterAPIView.as_view({'post': 'create'})),
    
]

