from rest_framework import routers
from django.urls import path
from applications.accounts.views import RoleApiView, UserAPIView

urlpatterns = [
    path('', RoleApiView.as_view({'get': 'list'})),
    path('register/', UserAPIView.as_view({'post': 'create'})),
    path('get-user/<int:pk>/', UserAPIView.as_view({'get': 'retrieve', 'put':'update'})),
    path('users/', UserAPIView.as_view({'get': 'list'}), name='user-list'),
]

