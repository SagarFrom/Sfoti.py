from django.shortcuts import render

# Create your views here.

from .models import Album
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from rest_framework import viewsets
from .serializers import AlbumSerializer,UserSerializer
from django.contrib.auth.models import User


class AlbumDetailView(DetailView):
	model = Album
	context_object_name = 'fav_album'
	template_name = 'albums.html'

class AlbumListView(ListView):
	model = Album
	context_object_name = 'albums'
	template_name = 'albums.html'
	
	  
class AlbumViewSet(viewsets.ModelViewSet):
	model = Album	
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer	

class UserViewSet(viewsets.ModelViewSet):	
	queryset = User.objects.all()
	serializer_class = UserSerializer	
