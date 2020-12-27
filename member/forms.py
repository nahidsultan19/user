from django import forms
from .models import *


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
