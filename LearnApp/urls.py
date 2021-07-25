
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth_reception/', include('rest_framework.urls')),
    path('api/', include('account.urls')),
    path('api/', include('app.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth_token/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
