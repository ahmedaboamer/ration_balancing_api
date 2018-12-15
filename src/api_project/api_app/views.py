from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions

# Create your views here.

class HelloAPIView(APIView):
    """docstring for HelloAPI."""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview = ['1- the first api',
        '2- the second api',
        '3- the third api']

        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'message':'put method'})

    def patch(self,request,pk=None):
        return Response({'message':'patch method'})

    def delete(self,request,pk=None):
        return Response({'message':'delete method'})

class HelloViewSet(viewsets.ViewSet):
    """docstring for HelloView."""
    serilaizer_class=serializers.HelloSerializer
    def list(self,request):
        a_view = [
        '1- the first in the list',
        '2- the second in the list',
        '3- the third in the list'
        ]

        return Response({'message':'Hello form viewsets','a_view':a_view})

    def create(self,request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'A new create message {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        return Response({'message':'GET method'})

    def update(self,request,pk=None):
        return Response({'message':'POST method'})

    def partial_update(self,request,pk=None):
        return Response({'message':'PATCH method'})

    def destroy(self,request,pk=None):
        return Respone({'message':'DELETE method'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """docstring for UserProfileViewSet."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request)
