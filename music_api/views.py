from django.utils.module_loading import import_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from rest_framework import generics, status, exceptions
from rest_framework.response import Response

from . import serializers
from .exceptions import InvalidToken, TokenError
#from musicapp.settings import AUTH_HEADER_TYPES, api_settings
from .models import Song
from .serializers import SongSerializer, TokenSerializer

# Create your views here.

class MusicLibraryView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PlaylistsView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DetailSongView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)

class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class RegisterUsersView(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)


"""
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            return Response({
                "token": jwt_encode_handler(jwt_payload_handler(user)),
                'username': username,
            }, status=200)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class JwtAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header:
            key, token = auth_header.split(' ')

            if key == 'Bearer':
                # Decode the token here. If it is valid, get the user instance associated with it and return it
                ...
                return User, None

                # If token exists but it is invalid, raise AuthenticationFailed exception

                # If token does not exist, return None so that another authentication class can handle authentication
"""

