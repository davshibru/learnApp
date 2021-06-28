from rest_framework import routers
from .views import CheckFirstLoginViewSet

router = routers.DefaultRouter()
router.register('accountchecker', CheckFirstLoginViewSet, basename='accountchecker')