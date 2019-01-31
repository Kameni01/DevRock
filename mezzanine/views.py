from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *



"""Класс вывода древа проектов на стартовой странице"""
class TreeRender(LoginRequiredMixin, View):
    def get(self, request):
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()

        return render(request, 'mezzanine/default.html', {"projects": projects, "pages": pages, 'sub_page': sub_pages})



"""Класс вывода подробной информации по странице проекта"""
class ProjectDetail(LoginRequiredMixin, View):
    def get(self, request, slug):
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        files = ProjectFiles.objects.all()
        sub_pages = ProjectPages.objects.all()
        project = get_object_or_404(Projects, slug=slug)

        return render(request, 'mezzanine/detailproject.html', {"projects": projects, "pages": pages, 'files': files, 'detail': project, 'sub_page': sub_pages})



"""Класс вывода подробной информации по странице проекта"""
class PageDetail(LoginRequiredMixin, View):
    def get(self, request, slug):
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        files = PageFiles.objects.all()
        sub_pages = ProjectPages.objects.all()
        page = ProjectPages.objects.get(slug__iexact=slug)

        return render(request, 'mezzanine/pagedetail.html', {"projects": projects, "pages": pages, 'files': files, 'detail': page, 'sub_page': sub_pages})



"""Класс для создания проектов"""
class CreateProject(LoginRequiredMixin, NonInheritedObjectCreateMixin, View):
    form_model = CreateProjectForm
    template = 'mezzanine/createproject.html'
    raise_exception = True


"""Класс для изменения проектов"""
class update_project(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Projects
    form_model = CreateProjectForm
    template = 'mezzanine/updateproject.html'
    raise_exception = True


"""Класс удаления проектов"""
class ProjectDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Projects
    template = 'mezzanine/deleteproject.html'
    redirect_url = 'mezzanine'
    raise_exception = True


"""Класс добавления файлов к проектам"""
class AddProjectFile(LoginRequiredMixin, InheritedObjectCreateMixin, View):
    form_model = Add_file_project
    template = 'mezzanine/addprojectfile.html'
    what = 'proj_file'
    raise_exception = True


class DeleteProjectFile(LoginRequiredMixin, FileDeleteMixin, View):
    model = ProjectFiles
    template = 'mezzanine/deleteprojectfile.html'
    redirect_url = 'mezzanine'
    raise_exception = True


"""Класс для создания страниц"""
class CreatePage(LoginRequiredMixin, InheritedObjectCreateMixin, View):
    form_model = CreatePageForm
    template = 'mezzanine/createpage.html'
    what = 'proj'
    raise_exception = True


"""Класс для создания страниц"""
class CreatePageToPage(LoginRequiredMixin, InheritedObjectCreateMixin, View):
    form_model = CreatePageForm
    template = 'mezzanine/createpagetopage.html'
    what = 'page'
    raise_exception = True


"""Класс для изменения страниц"""
class update_page(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = ProjectPages
    form_model = CreatePageForm
    template = 'mezzanine/updatepage.html'
    raise_exception = True


"""Класс удаления страниц"""
class PageDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = ProjectPages
    template = 'mezzanine/deletepage.html'
    redirect_url = 'mezzanine'
    raise_exception = True


"""Класс добавления файлов к проектам"""
class AddPageFile(LoginRequiredMixin, InheritedObjectCreateMixin, View):
    form_model = Add_file_page
    template = 'mezzanine/addpagefile.html'
    what = 'page_file'
    raise_exception = True


class DeletePageFile(LoginRequiredMixin, FileDeleteMixin, View):
    model = PageFiles
    template = 'mezzanine/deletepagefile.html'
    redirect_url = 'mezzanine'
    raise_exception = True
