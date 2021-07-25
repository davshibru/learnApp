from rest_framework import routers
from .views import GeniralTopicViewSet, TopicViewSet, CreateUserAccessViewSet, UserResultViewSet

router = routers.DefaultRouter()
router.register('geniral-topics', GeniralTopicViewSet, basename='getgeniraltopics')
router.register('topics', TopicViewSet, basename='topics')
router.register('create-user-access', CreateUserAccessViewSet, basename='createuseraccess')
router.register('add-user-results', UserResultViewSet, basename='userresult')
