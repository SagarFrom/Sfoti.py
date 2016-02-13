from rest_framework import serializers

from .models import Artist
from albums.serializers import AlbumSerializer
from tracks.serializers import TrackSerializer
	

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artist
		fileds = ('url','first_name','last_name','biography')

#class TrackSerializer(serializers.HyperlinkedModelSerializer):
#	class Meta:
#		model = Track
		