from django.forms import ModelForm, Form
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.exceptions import ValidationError

from .models import *


class TaskForm(ModelForm):
    # title = forms.CharField(max_length=160)
    # body = forms.CharField(max_length=160)  # SummernoteWidget()


    # status = forms.ChoiceField(widget=forms.RadioSelect, choices=statuses)

    # title.widget.attrs.update({"class":"form-control"})
    # body.widget.attrs.update({"rows":"3", "class":"form-control"})

    class Meta:
        model = Task
        fields = ['title', 'body', 'status', 'project']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'size': 80}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'size': 80}),
        }

    def save(self):
        new_task = Task.objects.create(
            title=self.cleaned_data["title"],
            body=self.cleaned_data["body"],
            status=self.cleaned_data["status"],
            project=self.cleaned_data["project"]
        )

        return new_task