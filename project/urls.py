from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from django.views.generic import RedirectView
from core.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
)

# Setup drf router
router = routers.DefaultRouter()


urlpatterns = [
    # Redirects
    path(
        '',
        RedirectView.as_view(url='/admin/'),
        name='home-redirect-admin'
    ),
    path(
        'accounts/login/',
        RedirectView.as_view(url='/admin/'),
        name='login-redirect-admin'
    ),
    
    # Apps
    path('admin/', admin.site.urls),
    
    # Drf
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
