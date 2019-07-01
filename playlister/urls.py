from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'playlister'

urlpatterns = [
    path('', views.index, name="index"),

    path('register/', views.UserFormView.as_view(), name="register"),

    path('login/', views.UserLoginView, name="login"),

    path('logout/', views.UserLogoutView, name="logout"),

    #playlist-edit related urls
    path('add-playlist/', views.add_playlist.as_view(), name="add_playlist"),

    path('delete-playlist/<int:pk>/', views.delete_playlist.as_view(), name="delete_playlist"),

    path('edit-playlist/<int:pk>/', views.edit_playlist.as_view(), name="edit_playlist"),

    #song-edit related urls
    path('<int:pk>/add-song/', views.add_song.as_view(), name="add_song"),

    path('delete-song/<int:pk>', views.delete_song.as_view(), name="delete_song"),

    path('edit-song/<int:pk>/', views.edit_song.as_view(), name="edit_song"),

    #url-edit related urls
    path('<int:pk>/add-url/', views.add_url.as_view(), name="add_url"),

    path('delete-url/<int:pk>', views.delete_url.as_view(), name="delete_url"),

    path('edit-url/<int:pk>/', views.edit_url.as_view(), name="edit_url"),

    #normal view urls
    path('<str:playlist_name>/', views.playlist, name="playlist"),

    path('<str:playlist_name>/<str:song_name>/', views.song, name="song"),
]
