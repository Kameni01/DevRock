from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.exceptions import ValidationError

from .models import *

class CreateProjectForm(ModelForm):
    """Класс для создания проектов"""
    class Meta:
        model = Projects
        fields = ('mainimg','title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': SummernoteWidget(),
        }



    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug не может быть назван create!')
        if Projects.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug должен быть уникальным. Slug с именем "{}" уже существует!'.format(new_slug))
        return new_slug



class CreatePageForm(ModelForm):
    """Класс для создания страниц проектов"""
    class Meta:
        model = ProjectPages
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': SummernoteWidget(),
        }



    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug не может быть назван create!')
        if ProjectPages.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug должен быть уникальным. Slug с именем "{}" уже существует!'.format(new_slug))
        return new_slug



class Add_file_page(ModelForm):
    """Класс формы для добавления файлов к страницам"""
    class Meta:
        model = PageFiles
        fields = ('title', 'file')



class Add_file_project(ModelForm):
    """Класс формы для добавления файлов к проектам"""
    class Meta:
        model = ProjectFiles
        fields = ('title', 'file')
