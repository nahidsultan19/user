from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


def userView(request):
    return render(request, 'index.html')


def Register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('register')
    return render(request, 'register.html', {'form': form})
