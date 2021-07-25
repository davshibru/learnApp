from django.shortcuts import render

from .models import Geniral_Topics, Topics, UserAccess, Lections, UserResults
from .serializers import UserResultSerializer1, UserResultDetailSerializer, getGeniralTopicSerializer, UserResultSerializer,  UserAccessSerializer, getTopicSerializer, LectionForm, LectionSerializer, LectionCreateSerializer, getIdTopicSerializer, getIdGeniralTopicSerializer, UserAccessSerializer
from .permissions import ActionBasedPermission
from rest_framework import viewsets, status, generics, status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication

from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

from account.models import Account

# Lection --------------------------------------------------------------------------------

def home(request):
    if request.method=="POST":
        form=LectionForm(request.POST)
        if form.is_valid():
            post=form.save()
            return render(request, 'app/index.html', {'form': form})
    form=LectionForm()
    return render(request, 'app/index.html', {'form': form})


def postdetail(request, postID):
    lection = Lections.objects.get(id=postID)
    return render(request, 'app/postdetail.html', {'post': lection})

@requires_csrf_token
def upload_image_view(request):
    f = request.FILES['image']
    fs = FileSystemStorage()
    filename=str(f).strip('.')[0]
    file = fs.save(filename, f)
    fileurl = fs.url(file)
    print(fileurl)
    return JsonResponse({'success':1, 'file':{'url':'http://localhost:8000' + fileurl}})



@csrf_exempt
def upload_file_view(request):
    f = request.FILES['file']
    fs = FileSystemStorage()
    ff = str(f).split('.')

    ext = ff[len(ff) - 1]
    filename = ''
    for i in ff:
        if i != ext:
            filename += i
    print(filename)
    file = fs.save(filename, f)
    fileurl = fs.url(file)
    print(fileurl)
    return JsonResponse(
        {'success':1, 'file': {'url': 'http://localhost:8000' + fileurl, 'size': fs.size(filename), 'name': str(f), 'extraction': ext}}
    )

# --------------------------------------------------------------------------------

# class UserCreate(generics.CreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = UserSerializer

class GeniralTopicViewSet(viewsets.ModelViewSet):

    queryset = Geniral_Topics.objects.all()
    serializer_class = getGeniralTopicSerializer



class TopicViewSet(viewsets.ModelViewSet):

    # queryset = Topics.objects.all()
    serializer_class = getTopicSerializer

    def get_queryset(self):
        userT = self.request.user.username

        userId = Account.objects.filter(username=userT).values('id')

        topicsF = UserAccess.objects.filter(account__in=userId).values('id')

        return Topics.objects.filter(id__in=topicsF)

class TopicViewSet1(viewsets.ModelViewSet):
    # queryset = Topics.objects.all()
    serializer_class = getTopicSerializer
    authentication_classes = (TokenAuthentication,)

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):


        userT = self.request.user.username

        userId = Account.objects.filter(username=userT).values('id')

        topicsF = UserAccess.objects.filter(account__in=userId).values('topics')

        return Topics.objects.filter( id__in=topicsF, slug=self.kwargs['slug'])


class getIdTopicViewSet(viewsets.ModelViewSet):
    serializer_class = getIdTopicSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)

    def get_queryset(self):

        return Topics.objects.filter(english_name=self.kwargs['slug'])
        # return Topics.objects.all()


class getIdGeniralTopicViewSet(viewsets.ModelViewSet):
    serializer_class = getGeniralTopicSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)

    def get_queryset(self):

        return Geniral_Topics.objects.filter(slug=self.kwargs['slug'])

class LectionViewSet(viewsets.ModelViewSet):
    serializer_class = LectionSerializer


    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):

        userT = self.request.user.username

        userId = Account.objects.filter(username=userT).values('id')

        topicsF = UserAccess.objects.filter(account__in=userId).values('topics')

        topic = self.kwargs['slug']
        topicId = Topics.objects.filter(english_name=topic, id__in=topicsF).values('id')

        return Lections.objects.filter(topics__in=topicId)



class LectionDitailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lections.objects.all()
    serializer_class = LectionSerializer
    lookup_field = 'slug'

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class LectionCreate(generics.CreateAPIView):
    queryset = Lections.objects.all()
    serializer_class = LectionCreateSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)

class TopicCreate(generics.CreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = getTopicSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)

class GeniralTopicCreate(generics.CreateAPIView):
    queryset = Geniral_Topics.objects.all()
    serializer_class = getGeniralTopicSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)



class GetAccessViewSet(viewsets.ModelViewSet):
    queryset = UserAccess.objects.all()
    serializer_class = UserAccessSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

class CreateUserAccessViewSet(viewsets.ModelViewSet):

    serializer_class = UserAccessSerializer
    model = UserAccess
    queryset = UserAccess.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = UserAccessSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserAcceseDitailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccess.objects.all()
    serializer_class = UserAccessSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

class UserResultDitailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserResults.objects.all()
    serializer_class = UserResultDetailSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    lookup_field = 'sluguser'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        userT = self.request.user.username
        lection = request.data['slug']
        account = Account.objects.filter(username=userT)
        lectionList = Lections.objects.filter(slug=lection)

        lectionId = lectionList.values('id')[0].get('id')
        accountId = account.values('id')[0].get('id')

        request.data['account'] = accountId
        request.data['lection'] = lectionId

        if (instance.score < request.data['score']):
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)

        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
            return Response(serializer.data)



    def get_queryset(self):

        lectionId = Lections.objects.filter(slug=self.kwargs['slug']).values('id')[0].get('id')
        accountId = Account.objects.filter(username=self.kwargs['sluguser']).values('id')[0].get('id')

        return UserResults.objects.filter(account=accountId, lection=lectionId)

class UserResultViewSet(viewsets.ModelViewSet):
    queryset = UserResults.objects.all()
    serializer_class = UserResultSerializer
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'slug'
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'create'],
        IsAdminUser: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }

    def list(self, request):
        lection = self.kwargs['slug']
        queryset = UserResults.objects.filter(slug=lection)
        serializer = UserResultSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        #many = True if isinstance(request.data, list) else False

        userT = self.request.user.username
        lection = request.data['slug']
        account = Account.objects.filter(username=userT)
        lectionList = Lections.objects.filter(slug=lection)

        lectionId = lectionList.values('id')[0].get('id')
        accountId = account.values('id')[0].get('id')

        # request.data._mutable = True
        request.data['account'] = accountId
        request.data['lection'] = lectionId
        # request.data._mutable = False

        serializer = UserResultSerializer(data=request.data)

        if serializer.is_valid():

            serializer.validated_data['sluguser'] = userT
            serializer.validated_data['slug'] = request.data['slug']
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)



class UserResultViewSet1(viewsets.ModelViewSet):
    queryset = UserResults.objects.all()
    serializer_class = UserResultSerializer1

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    def get_queryset(self):

        lection = self.kwargs['slug']

        return UserResults.objects.filter(slug=lection)




