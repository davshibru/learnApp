from django.shortcuts import render
from rest_framework.views import APIView
from .models import Account
from .serializers import CheckFirstLoginSerializer, UserSerializer, setFirstLoginSerializer, ChangePasswordSerializer
from .permissions import IsOwner
from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets, status, generics, status

class CheckFirstLoginViewSet(viewsets.ModelViewSet):

    #queryset = Account.objects.all()
    model = Account
    serializer_class = CheckFirstLoginSerializer
    permission_classes = ( IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        userT = self.request.user.username
        return Account.objects.filter(username=userT)

class FirstLoginDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = setFirstLoginSerializer
    queryset = Account.objects.all()
    permission_classes = (IsOwner,)
    authentication_classes = (TokenAuthentication,)

class UserCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)