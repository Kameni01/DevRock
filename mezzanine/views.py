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
    sub_pages = ProjectPages.objects.all()

    return render(request, 'mezzanine/default.html', {"projects": projects, "pages": pages, 'sub_page': sub_pages})



"""Функция вывода подробной информации по странице проекта"""
def ProjectDetail(request, slug):
    projects = Projects.objects.all()
    pages = ProjectPages.objects.all()
    files = ProjectFiles.objects.all()
    sub_pages = ProjectPages.objects.all()
    project = get_object_or_404(Projects, slug=slug)


    return render(request, 'mezzanine/detailproject.html', {"projects": projects, "pages": pages, 'files': files, 'detail': project, 'sub_page': sub_pages})



"""Функция вывода подробной информации по странице проекта"""
def PageDetail(request, slug):
    projects = Projects.objects.all()
    pages = ProjectPages.objects.all()
    files = PageFiles.objects.all()
    sub_pages = ProjectPages.objects.all()
    page = get_object_or_404(ProjectPages, slug=slug)


    return render(request, 'mezzanine/pagedetail.html', {"projects": projects, "pages": pages, 'files': files, 'detail': page, 'sub_page': sub_pages})



"""Класс для создания проектов"""
class CreateProject(NonInheritedObjectCreateMixin, View):
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
class AddProjectFile(InheritedObjectCreateMixin, View):
    form_model = Add_file_project
    template = 'mezzanine/addprojectfile.html'
    what = 'proj_file'



class DeleteProjectFile(FileDeleteMixin, View):
    model = ProjectFiles
    template = 'mezzanine/deleteprojectfile.html'
    redirect_url = 'mezzanine'



"""Класс для создания страниц"""
class CreatePage(InheritedObjectCreateMixin, View):
    form_model = CreatePageForm
    template = 'mezzanine/createpage.html'
    what = 'proj'



"""Класс для создания страниц"""
class CreatePageToPage(InheritedObjectCreateMixin, View):
    form_model = CreatePageForm
    template = 'mezzanine/createpagetopage.html'
    what = 'page'



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
class AddPageFile(InheritedObjectCreateMixin, View):
    form_model = Add_file_page
    template = 'mezzanine/addpagefile.html'
    what = 'page_file'



class DeletePageFile(FileDeleteMixin, View):
    model = PageFiles
    template = 'mezzanine/deletepagefile.html'
    redirect_url = 'mezzanine'
