from django.db import models
# from users.models import NewUser
from django.utils import timezone


# Create your models here.
class Song(models.Model):

    options = (
        ('others', 'Others'),
        ('hip hop', 'Hip Hop'),
        ('popular', 'Popular'),
        ('rock', 'Rock'),
        ('alternative rock', 'Alternative Rock'),
        ('country', 'Country'),
        ('pop', 'Pop'),
        ('classical', 'Classical'),
        ('rhythm and blues', 'Rhythm and Blues'),
        ('blues', 'Blues'),
        ('jazz', 'Jazz'),
        ('blues', 'Blues'),
        ('soul', 'Soul'),
        ('reggae', 'Reggae'),
        ('gospel', 'Gospel'),
        ('afrobeat', 'Afrobeat'),
        ('juju', 'Juju'),
        ('fuji', 'Fuji'),
    )

    album = models.CharField(max_length=255, blank=True)
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)
    genre = models.CharField(max_length=20, choices=options, default='others')
    lyrics = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)
    #owner = models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, related_name='playlist_songs')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)

