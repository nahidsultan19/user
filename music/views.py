from django.shortcuts import render
from django.http import HttpResponse


def MusicView(request):
    return HttpResponse('Hello Music App!')
