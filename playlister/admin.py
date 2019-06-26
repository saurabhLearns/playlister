from django.contrib import admin
from .models import Playlist, Song, SongLink

admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(SongLink)