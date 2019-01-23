from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.exceptions import ValidationError

from .models import Projects, ProjectPages

class CreateProjectForm(ModelForm):
    """Класс для создания проектов"""
    class Meta:
        model = Projects
        fields = ('mainimg','title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'text': SummernoteWidget(),
        }

    # def clean_title(self):
    #     new_title = self.cleaned_data['title']
    #
    #     if Projects.objects.filter(title__iexact=new_title).count():
    #         raise ValidationError('Проект с именем "{}" уже существует! Придумайте новое имя проекта...'.format(new_title))
    #     return new_title


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug не может быть назван create!')
        if Projects.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug должен быть уникальным. Slug с именем "{}" уже существует!'.format(new_slug))
        return new_slug



# class UpdateProjectForm(ModelForm):
#     """Класс для редактирования проектов"""
#     class Meta:
#         model = Projects
#         fields = ('mainimg','title', 'text')
#
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'text': SummernoteWidget(),
#         }
#
#     def clean_title(self):
#         new_title = self.cleaned_data['title']
#
#         if Projects.objects.filter(title__iexact=new_title).count():
#             raise ValidationError('Проект с именем "{}" уже существует! Придумайте новое имя проекта...'.format(new_title))
#         return new_title


class CreatePageForm(ModelForm):
    """Класс для создания страниц проектов"""
    class Meta:
        model = ProjectPages
        fields = ('project','title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'text': SummernoteWidget(),
        }

    # def clean_title(self):
    #     new_title = self.cleaned_data['title']
    #
    #     if ProjectPages.objects.filter(title__iexact=new_title).count():
    #         raise ValidationError('Проект с именем "{}" уже существует! Придумайте новое имя проекта...'.format(new_title))
    #     return new_title


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug не может быть назван create!')
        if ProjectPages.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug должен быть уникальным. Slug с именем "{}" уже существует!'.format(new_slug))
        return new_slug
