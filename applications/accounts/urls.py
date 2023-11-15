from rest_framework import routers
from django.urls import path
from applications.accounts.views import RegisterUserApiView

urlpatterns = [
    path('', RegisterUserApiView.as_view()),
]

