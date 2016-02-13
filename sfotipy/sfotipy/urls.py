"""sfotipy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns,include,url
from django.contrib import admin
admin.autodiscover()
from rest_framework import routers
from artists.views import ArtistDetailView,ArtistListView
from albums.views import AlbumDetailView,AlbumListView
from tracks.views import TrackViewSet

from artists.views import ArtistViewSet
from albums.views import AlbumViewSet , UserViewSet


router = routers.DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    
   url(r'^admin/', include(admin.site.urls)),
   url(r'^tracks/(?P<title>[\w\-]+)/', 'tracks.views.track_view',name='track_view'),
   #url(r'^artists/(?P<pk>[\d]+)',ArtistDetailView.as_view()),
   #url(r'^artists/', ArtistListView.as_view()),
        
   url(r'^api/', include(router.urls)),
   
   #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


#urlpatterns = patterns('',
#	url(r'^HelloWorld/',include('HelloWorld.urls')),
#	url(r'^admin/',include(admin.site.urls)),
#)
