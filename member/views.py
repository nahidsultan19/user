from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Member
from .forms import MemberForm


def MemberView(request):
    context = {
        'form': MemberForm()
    }
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('member-list')
    else:
        members = Member.objects.all()
    return render(request, 'member-form.html', context)


def MemberList(request):
    context = {
        'members': Member.objects.all()
    }
    return render(request, 'member-list.html', context)
