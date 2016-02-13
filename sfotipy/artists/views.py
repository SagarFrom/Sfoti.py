from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .serializers import ArtistSerializer

from .models import Artist
from rest_framework import viewsets
from rest_framework.response import Response

class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'fav_artist'
	template_name = 'artists.html'

class ArtistListView(ListView):
	model = Artist
	context_object_name = 'artists'
	template_name = 'artists.html'
	  
class ArtistViewSet(viewsets.ModelViewSet):
	model = Artist
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

	
 	