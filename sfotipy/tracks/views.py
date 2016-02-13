import json	
from django.shortcuts import render,get_object_or_404 
from django.http import HttpResponse,Http404
from .models import Track
from tracks.serializers import TrackSerializer
# Create your views here.

def track_view(request, title):
	
	track = get_object_or_404(Track,title=title)
	bio = track.artist.biography

	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
			'name': track.artist.first_name,
			'bio': bio,

		}

	}

	json_data = json.dumps(data)

	return HttpResponse(json_data,content_type='application/json')

from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
	model = Track
	queryset = Track.objects.all()
	serializer_class = TrackSerializer	
 	
	#try:
	#	track = Track.objects.get(title=title)
	#	bio = track.artist.biography

	#except Track.DoesNotExist:		
	#	raise Http404

	#return render(request,'track.html', {'track' : track,'bio' : bio})
	
	########

	#return HttpResponse('Ok')
	
	
	#shortcat
	#track = get_object_or_404(Track,title=title)

	


	