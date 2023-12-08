from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from applications.accounts.views import MyTokenObtainView, ProfileApiView
from rest_framework import routers
from applications.jobs.views import JobsApiView, EmployerJobsApiView
from applications.proffessional.views import ExperienceApiView, EducationApiView
from django.conf.urls.static import static
from careernest import settings
from django.conf import settings


router = routers.DefaultRouter()

router.register('jobs', JobsApiView, basename='jobs')
router.register('employer/jobs', EmployerJobsApiView, basename='employer_jobs')
router.register('profile', ProfileApiView, basename="profile")
router.register('experience', ExperienceApiView, basename="experience")
router.register('education', EducationApiView, basename="experience")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', MyTokenObtainView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('applications.accounts.urls')),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)