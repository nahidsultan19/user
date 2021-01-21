from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusicView, name='music-index'),
    path('music-list/', views.MusicList, name='music-list'),
    path('music-update/<str:pk>/', views.UpdateMusic, name='music-update'),
    path('music-delete/<str:pk>/', views.MusicDelete, name='music-delete')
]
