from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from applications.accounts.views import MyTokenObtainView, ProfileApiView
from rest_framework import routers
from applications.jobs.views import JobsApiView, EmployerJobsApiView


router = routers.DefaultRouter()


router.register('jobs', JobsApiView, basename='jobs')
router.register('employer/jobs', EmployerJobsApiView, basename='employer_jobs')
router.register('profile', ProfileApiView, basename="profile")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', MyTokenObtainView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('applications.accounts.urls')),
    path('', include(router.urls)),
]