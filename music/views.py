from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import MusicForm


def MusicView(request):
    context = {
        'form': MusicForm()
    }
    return render(request, 'music-form.html', context)
