from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from applications.accounts.serializers.token_serializer import MyTokenObtainPairSerializer
from applications.accounts.views import MyTokenObtainView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/login/', TokenObtainPairView.as_view(serializer_class=MyTokenObtainPairSerializer), name='token_obtain_pair'),
    path('accounts/login/', MyTokenObtainView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('applications.accounts.urls')),
]