from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberView, name='form-page'),
    path('member/', views.MemberList, name='member-list')
]
