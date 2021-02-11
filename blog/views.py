from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'NahidS',
        'title': 'Learn Python',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores eos soluta.',
        'date_posted': 'February 2, 2021'
    },
    {
        'author': 'ShirenAK',
        'title': 'Learn JavaScript',
        'content': 'First Javascript post',
        'date_posted': 'February 2, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})
