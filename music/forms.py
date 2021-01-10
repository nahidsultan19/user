from django import forms
from .models import *


class MusicForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
