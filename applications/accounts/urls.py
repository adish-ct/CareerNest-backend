from rest_framework import routers
from django.urls import path
from applications.accounts.views import RoleApiView, UserAPIView, HomeView, OtpValidationView

urlpatterns = [
    path('', RoleApiView.as_view({'get': 'list'})),
    path('register/', UserAPIView.as_view({'post': 'create'})),
    path('user-verification/', OtpValidationView.as_view(), name='user_verification'),
     path('get-user/<int:pk>/', UserAPIView.as_view({'get': 'retrieve', 'put':'update'})),
    path('users/', UserAPIView.as_view({'get': 'list', 'put': 'update'}), name='user-list'),
    path('home/', HomeView.as_view(), name='home')
]

