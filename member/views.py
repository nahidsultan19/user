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


def MemberUpdate(request, pk):
    member = Member.objects.get(id=pk)
    form = MemberForm(instance=member)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
        return redirect('member-list')
    context = {'form': form}
    return render(request, 'member-update.html', context)
