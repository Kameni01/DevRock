from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic import View

from .models import *
from .forms import *
from .utils import *



"""Функция вывода древа проектов на стартовой странице"""
def TreeRender(request):
    projects = Projects.objects.all()
    pages = ProjectPages.objects.all()


    return render(request, 'mezzanine/default.html', {"projects": projects, "pages": pages})



"""Функция вывода подробной информации по странице проекта"""
def ProjectDetail(request, slug):
    projects = Projects.objects.all()
    pages = ProjectPages.objects.all()
    files = ProjectFiles.objects.all()
    project = get_object_or_404(Projects, slug=slug)


    return render(request, 'mezzanine/detailproject.html', {"projects": projects, "pages": pages, 'files': files, 'detail': project})



"""Функция вывода подробной информации по странице проекта"""
def PageDetail(request, slug):
    projects = Projects.objects.all()
    pages = ProjectPages.objects.all()
    files = PageFiles.objects.all()
    page = get_object_or_404(ProjectPages, slug=slug)


    return render(request, 'mezzanine/pagedetail.html', {"projects": projects, "pages": pages, 'files': files, 'detail': page})



"""Класс для создания проектов"""
class CreateProject(ObjectCreateMixin, View):
    form_model = CreateProjectForm
    template = 'mezzanine/createproject.html'



"""Класс для изменения проектов"""
class update_project(ObjectUpdateMixin, View):
    model = Projects
    form_model = CreateProjectForm
    template = 'mezzanine/updateproject.html'



"""Класс удаления проектов"""
class ProjectDelete(ObjectDeleteMixin, View):
    model = Projects
    template = 'mezzanine/deleteproject.html'
    redirect_url = 'mezzanine'



"""Класс добавления файлов к проектам"""
class AddProjectFile(ObjectCreateMixin, View):
    form_model = Add_file_project
    template = 'mezzanine/addprojectfile.html'



class DeletePageFile(FileDeleteMixin, View):
    model = PageFiles
    template = 'mezzanine/deleteprojectfile.html'
    redirect_url = 'mezzanine'



"""Класс для создания страниц"""
class CreatePage(ObjectCreateMixin, View):
    form_model = CreatePageForm
    template = 'mezzanine/createpage.html'



"""Класс для изменения страниц"""
class update_page(ObjectUpdateMixin, View):
    model = ProjectPages
    form_model = CreatePageForm
    template = 'mezzanine/updatepage.html'



"""Класс удаления страниц"""
class PageDelete(ObjectDeleteMixin, View):
    model = ProjectPages
    template = 'mezzanine/deletepage.html'
    redirect_url = 'mezzanine'



"""Класс добавления файлов к проектам"""
class AddPageFile(ObjectCreateMixin, View):
    form_model = Add_file_page
    template = 'mezzanine/addpagefile.html'



class DeletePageFile(FileDeleteMixin, View):
    model = PageFiles
    template = 'mezzanine/deletepagefile.html'
    redirect_url = 'mezzanine'
