from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Playlist, Song, SongLink

#normal views
def index(request):
    all_playlists = Playlist.objects.all()
    return render(request, 'playlister/index.html', {'all_playlists' : all_playlists,})


def playlist(request, playlist_name):
    current_playlist_name = get_object_or_404 (Playlist, name = playlist_name)
    return render(request, 'playlister/songs.html', {'current_playlist_name' : current_playlist_name})


def song(request, playlist_name, song_name):
    current_song_name = get_object_or_404(Song, song_name = song_name)
    current_playlist_name = get_object_or_404 (Playlist, name = playlist_name)
    return render(request, 'playlister/urls.html', {'current_song_name' : current_song_name, 'current_playlist_name' : current_playlist_name})

#playlist manipulation views
class add_playlist(CreateView):
    model = Playlist
    fields = ['name', 'mood', 'desc']


class edit_playlist(UpdateView):
    model = Playlist
    fields = ['name', 'mood', 'desc']


class delete_playlist(DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlister:index')


#song manipulation views
class add_song(CreateView):
    model = Song
    fields = ['song_name']
    def form_valid(self, form):
        form.instance.playlist = Playlist.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)


class delete_song(DeleteView):
    model = Song
    success_url = reverse_lazy('playlister:index')


class edit_song(UpdateView):
    model = Song
    fields = ['song_name']


#url manipulation views
class add_url(CreateView):
    model = SongLink
    fields = ['streaming_service_name', 'streaming_service_url']
    def form_valid(self, form):
        form.instance.song = Song.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)


class delete_url(DeleteView):
    model = SongLink
    success_url = reverse_lazy('playlister:index')


class edit_url(UpdateView):
    model = SongLink
    fields = ['streaming_service_name', 'streaming_service_url']