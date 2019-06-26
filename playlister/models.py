from django.db import models
from django.urls import reverse, reverse_lazy


class Playlist(models.Model):
    name = models.CharField(max_length=10)
    mood = models.CharField(max_length=10, blank = True)
    desc = models.CharField(max_length=200, blank = True)
    
    def get_absolute_url(self):
        return reverse('playlister:index')
    def __str__(self):
        return self.name


class Song(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('playlister:playlist', kwargs={'playlist_name': self.playlist.name})

    def __str__(self):
        return self.id


class SongLink(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    streaming_service_name = models.CharField(max_length=250) 
    streaming_service_url = models.CharField(max_length=2000)
    
    def get_absolute_url(self):
        return reverse('playlister:song', kwargs={'playlist_name': self.song.playlist.name, 'song_name' : self.song.song_name })