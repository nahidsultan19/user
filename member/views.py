from django.shortcuts import render, redirect
from django.http import HttpResponse

# message module
from django.contrib import messages

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
            messages.success(request, f'Information Successfully Submitted!')
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
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member successfully Updated!')
        return redirect('member-list')
    context = {'form': form}
    return render(request, 'member-update.html', context)


def MemberDelete(request, pk):
    member_delete = Member.objects.get(id=pk)
    if request.method == 'POST':
        member_delete.delete()
        messages.warning(request, f'Member Deleted!')
        return redirect('member-list')
    context = {'member_delete': member_delete}
    return render(request, 'member-delete.html', context)
