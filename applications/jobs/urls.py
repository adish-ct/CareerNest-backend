from rest_framework import routers
from django.urls import path
from applications.jobs.views import RoleApiView

urlpatterns = [
    path('', RoleApiView.as_view())
]

