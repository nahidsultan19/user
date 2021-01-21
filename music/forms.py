from django import forms
from .models import *


class MusicForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
        labels = {
            'title': 'Song Title',
        }

    def __init__(self, *args, **kwargs):
        super(MusicForm, self).__init__(*args, **kwargs)
        self.fields['artist_name'].empty_label = 'Select'
        self.fields['album_title'].empty_label = 'Select'
