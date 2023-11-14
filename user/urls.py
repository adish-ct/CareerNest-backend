from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user.views import RegisterUserApiView

router = DefaultRouter()
# router.register(r"employer/register", EmployerRegisterViewSet, basename="employer-register")

urlpatterns = [
    # path("user/", include(router.urls)),
    path("register/", RegisterUserApiView.as_view()),
]