from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Playlist, Song, SongLink
from . import forms

#normal views
def index(request):
    all_playlists = Playlist.objects.all()
    try:
        username = request.session['username']
    except KeyError:
        return render(request, 'playlister/index.html', {'all_playlists' : all_playlists,})
    return render(request, 'playlister/index.html', {'all_playlists' : all_playlists, 'username' : username})


def playlist(request, playlist_name):
    current_playlist_name = get_object_or_404 (Playlist, name = playlist_name)
    try:
        username = request.session['username']
    except KeyError:
        return render(request, 'playlister/songs.html', {'current_playlist_name' : current_playlist_name,})
    return render(request, 'playlister/songs.html', {'current_playlist_name' : current_playlist_name, 'username' : username})


def song(request, playlist_name, song_name):
    current_song_name = get_object_or_404(Song, song_name = song_name)
    current_playlist_name = get_object_or_404 (Playlist, name = playlist_name)
    try:
        username = request.session['username']
    except KeyError:
        return render(request, 'playlister/urls.html', {'current_song_name' : current_song_name, 'current_playlist_name' : current_playlist_name})
        return render(request, 'playlister/urls.html', {'current_song_name' : current_song_name, 'current_playlist_name' : current_playlist_name, 'username' : username})

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


#userlogin
class UserFormView(View):
    form_class = forms.UserForm
    template_name = 'playlister/register.html'
    def get(self, request):
        try:
            username = self.request.session['username']
            return redirect('playlister:index')
        except KeyError:
            form = self.form_class(None)
            return render(request, self.template_name,{'form' : form})

    def post(self, request):
        try:
            username = self.request.session['username']
            return redirect('playlister:index')
        except KeyError:
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                return redirect('playlister:index')
            else:
                return render(request, self.template_name,{'form' : form})



def UserLoginView(request):
    try:
        username = request.session['username']
        return redirect('playlister:index')
    except KeyError:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = username
                    return redirect('playlister:index')
        return render(request, 'playlister/login.html')


def UserLogoutView(request):
    del request.session['username']
    logout(request)
    return render(request, 'playlister/login.html')