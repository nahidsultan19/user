from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusicView, name='music-index')
]
