from django import forms
from .models import Audios


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audios
        fields = ('title', 'category', 'audio')
    
    
class SearchAudio(forms.ModelForm):
    class Meta:
        model= Audios
        fields = ('category', 'title') 