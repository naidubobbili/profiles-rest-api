from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    '''test api view'''

    def get(self,request,format=None):
        '''returns a list of APIView features'''
        an_apiview=[

        'Uses HTTP methods as function (get,post,patch,put,delete)'
        'Is similar to a traditional Django View',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLs',
        'created by me',


        ]


        return Response({'message':'hello','an_apiview':an_apiview})
