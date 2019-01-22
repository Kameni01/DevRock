from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import Projects, ProjectPages, ProjectFiles, PageFiles
#from .forms import

def TreeRender(request):
    """Функция вывода древа проектов на стартовой странице"""
    projects = Projects.objects.all()
    pages = ProjectPages.objects.all()

    return render(request, 'mezzanine/default.html', {"projects": projects, "pages": pages})



def ProjectDetail(request, slug):
    """Функция вывода подробной информации по странице проекта"""
    projects = Projects.objects.all()
    pages = ProjectPages.objects.all()
    files = ProjectFiles.objects.all()
    project = get_object_or_404(Projects, slug=slug)


    return render(request, 'mezzanine/detailproject.html', {"projects": projects, "pages": pages, 'files': files, 'detail': project})



def PageDetail(request, slug):
    """Функция вывода подробной информации по странице проекта"""
    projects = Projects.objects.all()
    pages = ProjectPages.objects.all()
    files = PageFiles.objects.all()
    page = get_object_or_404(ProjectPages, slug=slug)


    return render(request, 'mezzanine/pagedetail.html', {"projects": projects, "pages": pages, 'files': files, 'detail': page})
