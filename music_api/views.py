from django.shortcuts import render
from rest_framework import generics
from .models import Song
from .serializers import SongSerializer

# Create your views here.

class MusicLibraryView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PlaylistsView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class DetailSongView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

