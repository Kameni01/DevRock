from django.forms import ModelForm, Form
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.exceptions import ValidationError

from .models import *


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'body', 'status', 'project', 'deadline_date', 'executors']

        labels = {
            'title': 'Название',
            'body': 'Описание',
            'status': 'Статус',
            'project': 'Проект',
            'deadline_date': 'Дедлайн',
            'executors': 'Исполнители'
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'deadline_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'executors': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


class CommentForm(ModelForm):
    class Meta:
        model = TaskComment
        fields = ['body']

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }