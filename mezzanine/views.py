from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *



class TreeRender(LoginRequiredMixin, View):
    """Класс вывода древа проектов на стартовой странице"""
    def get(self, request):
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()

        return render(request, 'mezzanine/default.html', {"projects": projects, "pages": pages, 'sub_page': sub_pages})



class ProjectDetail(LoginRequiredMixin, View):
    """Класс вывода подробной информации по странице проекта"""
    def get(self, request, slug):
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        files = ProjectFiles.objects.all()
        sub_pages = ProjectPages.objects.all()
        project = get_object_or_404(Projects, slug=slug)

        return render(request, 'mezzanine/detailproject.html', {"projects": projects, "pages": pages, 'files': files, 'detail': project, 'sub_page': sub_pages})



class PageDetail(LoginRequiredMixin, View):
    """Класс вывода подробной информации по странице проекта"""
    def get(self, request, slug):
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        files = PageFiles.objects.all()
        sub_pages = ProjectPages.objects.all()
        page = ProjectPages.objects.get(slug__iexact=slug)

        return render(request, 'mezzanine/pagedetail.html', {"projects": projects, "pages": pages, 'files': files, 'detail': page, 'sub_page': sub_pages})



class CreateProject(LoginRequiredMixin, NonInheritedObjectCreateMixin, View):
    """Класс для создания проектов"""
    form_model = CreateProjectForm
    template = 'mezzanine/createproject.html'
    raise_exception = True



class UpdateProject(LoginRequiredMixin, ObjectUpdateMixin, View):
    """Класс для изменения проектов"""
    model = Projects
    form_model = CreateProjectForm
    template = 'mezzanine/updateproject.html'
    raise_exception = True



class ProjectDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """Класс удаления проектов"""
    model = Projects
    template = 'mezzanine/deleteproject.html'
    redirect_url = 'mezzanine'
    raise_exception = True



class AddProjectFile(LoginRequiredMixin, InheritedObjectCreateMixin, View):
    """Класс добавления файлов к проектам"""
    form_model = Add_file_project
    template = 'mezzanine/addprojectfile.html'
    what = 'proj_file'
    raise_exception = True



class DeleteProjectFile(LoginRequiredMixin, FileDeleteMixin, View):
    """Класс удаления файлов из проектов"""
    model = ProjectFiles
    template = 'mezzanine/deleteprojectfile.html'
    redirect_url = 'mezzanine'
    raise_exception = True



class CreatePage(LoginRequiredMixin, InheritedObjectCreateMixin, View):
    """Класс для создания страниц"""
    form_model = CreatePageForm
    template = 'mezzanine/createpage.html'
    what = 'proj'
    raise_exception = True



class CreatePageToPage(LoginRequiredMixin, InheritedObjectCreateMixin, View):
    """Класс для создания страниц"""
    form_model = CreatePageForm
    template = 'mezzanine/createpagetopage.html'
    what = 'page'
    raise_exception = True



class UpdatePage(LoginRequiredMixin, ObjectUpdateMixin, View):
    """Класс для изменения страниц"""
    model = ProjectPages
    form_model = CreatePageForm
    template = 'mezzanine/updatepage.html'
    raise_exception = True



class PageDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """Класс удаления страниц"""
    model = ProjectPages
    template = 'mezzanine/deletepage.html'
    redirect_url = 'mezzanine'
    raise_exception = True



class AddPageFile(LoginRequiredMixin, InheritedObjectCreateMixin, View):
    """Класс добавления файлов к страницам"""
    form_model = Add_file_page
    template = 'mezzanine/addpagefile.html'
    what = 'page_file'
    raise_exception = True



class DeletePageFile(LoginRequiredMixin, FileDeleteMixin, View):
    """Класс для удаления файлов со страниц"""
    model = PageFiles
    template = 'mezzanine/deletepagefile.html'
    redirect_url = 'mezzanine'
    raise_exception = True
