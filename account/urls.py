from django.contrib import admin
from django.urls import path, include
from .views import UserCreate, FirstLoginDetailView, ChangePasswordView
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', UserCreate.as_view()),
    path('accountchecker/<int:pk>', FirstLoginDetailView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]












#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('app/', DoctorView.as_view())
# ]
