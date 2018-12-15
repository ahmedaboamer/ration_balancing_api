from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPIView(APIView):
    """docstring for HelloAPI."""
    def get(self,request,format=None):
        an_apiview = ['1- the first api',
        '2- the second api',
        '3- the third api']

        return Response({'message':'hello','an_apiview':an_apiview})
