from rest_framework import serializers

from django.contrib.auth.models import User,Group
from .models import Album

#from artists.serializers import ArtistSerializer
from tracks.serializers import TrackSerializer


#ModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups','last_name')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):

	#url = serializers.HyperlinkedIdentityField(view_name='<artist></artist>-list')

	class Meta:
		model = Album
		fileds = ('url','id','title','cover')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



