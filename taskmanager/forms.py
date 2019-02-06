from django.forms import ModelForm, Form
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.exceptions import ValidationError

from .models import *


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'body', 'status', 'project']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = TaskComment
        fields = ['body']

        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }