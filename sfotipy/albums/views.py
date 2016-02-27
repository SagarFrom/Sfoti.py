from django.shortcuts import render

# Create your views here.

from .models import Album
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from rest_framework import viewsets
from .serializers import AlbumSerializer,UserSerializer
											
from django.contrib.auth.models import User

from django.views.generic import View 
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.forms.models import modelform_factory

from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt

class AlbumDetailView(DetailView):
	model = Album
	context_object_name = 'fav_album'
	template_name = 'albums.html'

class AlbumListView(ListView):
	model = Album
	context_object_name = 'albums'
	template_name = 'albums.html'
	
class AlbumViewSet(viewsets.ModelViewSet):
	#model = Album

	queryset = Album.objects.all()
	serializer_class = AlbumSerializer	

class UserViewSet(viewsets.ModelViewSet):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    model = User    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
    #@csrf_exempt
    #def update(self , request , pk):
    #    try:
    #        snippet = User.objects.get(pk=pk)
    #    except snippet.DoesNotExist:
    #        return Response(status=status.HTTP_404_NOT_FOUND)

    #   if request.method == 'GET':
    #       serializer = UserSerializer(snippet,context={'request': request})
    #       return Response(serializer.data)

    #   elif request.method == 'PUT':
    #       serializer = UserSerializer(snippet,context={'request': request}, data=request.data)
    #       if serializer.is_valid():
    #           serializer.save()
    #           return Response(serializer.data)
    #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	#deendencies = [
       
    #   ('contenttypes', 'album/json'),
    #
#@csrf_exempt
#def ser_detail(request, pk):
#
#    model = User    
#    queryset = User.objects.all()
#    
#    try:
#        snippet = User.objects.get(pk=pk)
#    except Snippet.DoesNotExist:
#        return HttpResponse(status=404)
#
#    if request.method == 'GET':
#        serializer = UserSerializer(snippet)
#        return JSONResponse(serializer.data)
#
#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = UserSerializer(snippet, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JSONResponse(serializer.data)
#        return JSONResponse(serializer.errors, status=400)
#
#    elif request.method == 'DELETE':
#        snippet.delete()
#        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
#@authentication_classes(SessionAuthentication)
#@permission_classes(IsAuthenticated)
def Userlist(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    context={'request': request}

    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets,context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
#@authentication_classes(SessionAuthentication)
#@permission_classes(IsAuthenticated)
def UserDetailView(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """

    try:
        snippet = User.objects.get(pk=pk)
    except snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(snippet,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(snippet,context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #elif request.method == 'DELETE':
     #   snippet.delete()
      #  return Response(status=status.HTTP_204_NO_CONTENT)