from django.contrib import admin
from django.urls import path, include
from playlister import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playlister/', include('playlister.urls')),
    #path('', views.index, name="index"),
]
