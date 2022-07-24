from django.contrib import admin
from django.urls import path, include
from .router import router
from django.views.decorators.csrf import csrf_exempt
from .views import UserResultDitailViewSet, UserResultViewSet1, UserResultViewSet, UserAcceseDitailViewSet, upload_image_view, upload_file_view, home, postdetail, LectionViewSet, LectionDitailViewSet, LectionCreate, getIdTopicViewSet, TopicCreate, getIdGeniralTopicViewSet, GeniralTopicCreate, GetAccessViewSet, CreateUserAccessViewSet

from .views import TopicViewSet1
urlpatterns = [
    path('', home),
    path('pd/<int:postID>/', postdetail),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('topics/<slug:slug>/', TopicViewSet1.as_view({'get': 'list'}), name='topics'),
    path('lection/<slug:slug>/', LectionViewSet.as_view({'get': 'list'}), name='lection'),
    path('detail-lection/<slug:slug>', LectionDitailViewSet.as_view(),name='lection-detail'),
    path('api/user-result/<slug:slug>/<slug:sluguser>/', UserResultDitailViewSet.as_view(), name='user-result'),
    path('create/lection/', LectionCreate.as_view()),
    path('create/topic/', TopicCreate.as_view()),
    path('create/geniral-topic/', GeniralTopicCreate.as_view()),
    path('fileUpload/', csrf_exempt(upload_file_view)),
    path('imageUpload/', csrf_exempt(upload_image_view)),
    path('get-topic-id/<slug:slug>', getIdTopicViewSet.as_view({'get': 'list'})),
    path('get-geniral-topic-id/<slug:slug>/', getIdGeniralTopicViewSet.as_view({'get': 'list'})),
    path('get-user-access/', GetAccessViewSet.as_view({'get': 'list'})),
    path('delete-user-access/<int:pk>/', UserAcceseDitailViewSet.as_view()),
    path('api/user-results/<slug:slug>/', UserResultViewSet1.as_view({'get': 'list'}), name='result')

]












#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('app/', DoctorView.as_view())
# ]
