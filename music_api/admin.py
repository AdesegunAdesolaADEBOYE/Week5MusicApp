from django.contrib import admin
from music_api.models import Song
from django.forms import TextInput, Textarea, CharField
from django.db import models


# Register your models here.
class SongAdminConfig(admin.ModelAdmin):
    model = Song
    search_fields = ('album', 'title', 'artist', 'genre',)
    list_filter = ('album', 'title', 'artist', 'genre', 'created', 'modified')
    ordering = ('-created',)
    list_display = ('title', 'id', 'artist', 'genre', 'created', 'modified')
    fieldsets = (
        (None, {'fields': ('album', 'title', 'artist',)}),
        ('Permissions', {'fields': ('created', 'modified')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('album', 'title', 'artist', 'genre', 'lyrics', 'created', 'modified',)}
        ),
    )

admin.site.register(Song, SongAdminConfig)

