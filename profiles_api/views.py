from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""


    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methodss ass function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most controll over your app logic',
            'It mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
