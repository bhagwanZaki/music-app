from django import forms
from django.forms import ModelForm
from .models import songs


class musicForm(ModelForm):
    prefix = 'Class'
    class Meta:
        model = songs
        fields = ['music','thubnail']
