from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from core.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
)
from blog import views as blog_views

# Setup drf router
router = routers.DefaultRouter()
router.register(r'groups', blog_views.GroupViewSet)
router.register(r'categories', blog_views.CategoryViewSet)
router.register(r'posts', blog_views.PostViewSet)


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

if not settings.STORAGE_AWS:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)