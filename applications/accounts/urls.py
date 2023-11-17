from rest_framework import routers
from django.urls import path
from applications.accounts.views import RoleApiView, UserRegisterAPIView

urlpatterns = [
    path('', RoleApiView.as_view({'get': 'list'})),
    path('register/', UserRegisterAPIView.as_view({'post': 'create'})),
]

