from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages

from .models import *
from .forms import MusicForm


def MusicView(request):
    context = {
        'form': MusicForm()
    }
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Information Successfully Submitted!')
        return redirect('music-list')
    return render(request, 'music-form.html', context)


def MusicList(request):
    context = {
        'tracks': Track.objects.all()
    }
    return render(request, 'music-list.html', context)


def UpdateMusic(request, pk):
    track = Track.objects.get(id=pk)
    form = MusicForm(instance=track)
    if request.method == 'POST':
        form = MusicForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            messages.success(request, f'Music successfully Updated!')
        return redirect('music-list')
    context = {'form': form}
    return render(request, 'music-update.html', context)


def MusicDelete(request, pk):
    delete_track = Track.objects.get(id=pk)
    if request.method == 'POST':
        delete_track.delete()
        messages.warning(request, f'Track Deleted!')
        return redirect('music-list')
    context = {'delete_track': delete_track}
    return render(request, 'music-delete.html', context)
