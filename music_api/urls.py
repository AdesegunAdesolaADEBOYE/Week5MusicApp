#from django.urls import path
from .views import MusicLibrary
from rest_framework.routers import DefaultRouter

app_name = 'music_api'

router = DefaultRouter()
router.register('', MusicLibrary, basename='song')
urlpatterns = router.urls

# urlpatterns = [
#     path('library/', MusicLibraryView.as_view(), name="musiclibrary-songs"),
#     path('songs/', PlaylistsView.as_view(), name="playlist-songs"),
#     path('<int:pk>/', DetailSongView.as_view(), name="song-detail"),
# ]

