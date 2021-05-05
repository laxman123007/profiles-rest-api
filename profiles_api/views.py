from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
        'Uses Http methods as function(get, post, patch, put, delete)',
        'Is similar to a traditional django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hellow message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Updating an object"""
        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        """Handles Partial update of an Object"""
        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'Method': 'DELETE'})


class HelloViewSet(ViewSet):
    """Test API VIEW SET"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        # raise Exception("Bye")
        """Return a Hello Method"""
        a_viewset = [
        'Uses actions(list, cteate, retrieve, update, patial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                status= status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle Getting an object by Its ID"""
        return Response({'Method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'Method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'Method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an Object"""
        return Response({'Method': 'DELETE'})
