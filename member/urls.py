from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberView, name='form-page'),
    path('member/', views.MemberList, name='member-list'),
    path('update/<str:pk>/', views.MemberUpdate, name='member-update'),
    path('delete/<str:pk>/', views.MemberDelete, name='member-delete')
]
