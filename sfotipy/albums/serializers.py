from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Album

#ModelSerializer
class AlbumSerializer(serializers.HyperlinkedModelSerializer):

	#url = serializers.HyperlinkedIdentityField(view_name='<artist></artist>-list')

	class Meta:
		model = Album
		fileds = ('url','id','title','cover')
		
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fileds = ('url','id')

