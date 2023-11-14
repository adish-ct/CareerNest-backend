from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user.views import EmployerRegisterViewSet

router = DefaultRouter()
# router.register(r"employer/register", EmployerRegisterViewSet, basename="employer-register")

urlpatterns = [
    # path("user/", include(router.urls)),
    path("employer/register", EmployerRegisterViewSet.as_view()),
]