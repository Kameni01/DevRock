from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.exceptions import ValidationError

from .models import *



class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','name', 'family', 'stack')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'family': forms.TextInput(attrs={'class': 'form-control'}),
            'stack': forms.TextInput(attrs={'class': 'form-control'}),
        }
