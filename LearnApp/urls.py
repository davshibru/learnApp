
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth_reception/', include('rest_framework.urls')),
    path('api/', include('account.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth_token/', include('djoser.urls.authtoken')),
]
