from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview=[
            'Uses HTTP method as functions',
            'Is similar to a traditional Django View',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello','ans_apiview':an_apiview})

    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class=serializers.HelloSerializer

    def list(self,request):
        a_viewset=[
            'Uses actions',
            'Maps to Urls',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):

        return Response({'http_method':'GET'})

    def update(Self,request,pk=None):

        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):

        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)
