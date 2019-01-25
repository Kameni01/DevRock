from django.shortcuts import render, get_object_or_404, redirect
from .models import *



"""Класс наследуемый для создания объектов ничего
не наследующих от других объектов"""
class NonInheritedObjectCreateMixin:
    form_model = None
    template = None
    def get(self, request):
        form = self.form_model()
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()

        return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages, 'sub_page': sub_pages})

    def post(self, request):
        form = self.form_model(request.POST, request.FILES)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()

        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages, 'sub_page': sub_pages})



"""Класс наследуемый для создания объектов наслудющих
ключи других объектов автоматически"""
class InheritedObjectCreateMixin:
    form_model = None
    template = None
    def get(self, request, slug):
        form = self.form_model()
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()
        if self.what == 'proj':
            obj = Projects.objects.get(slug__iexact=slug)
        elif self.what == 'page':
            obj = ProjectPages.objects.get(slug__iexact=slug)
        elif self.what == 'proj_file':
            obj = Projects.objects.get(slug__iexact=slug)
        elif self.what == 'page_file':
            obj = ProjectPages.objects.get(slug__iexact=slug)
        else:
            obj = None
        return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages, 'obj': obj, 'sub_page': sub_pages})

    def post(self, request, slug):
        form = self.form_model(request.POST, request.FILES)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()

        if form.is_valid():
            if self.what == 'proj':
                obj = Projects.objects.get(slug__iexact=slug)
                form.instance.project_id = obj.id
            elif self.what == 'page':
                obj = ProjectPages.objects.get(slug__iexact=slug)
                form.instance.project_id = obj.project_id
                form.instance.parent_page = obj.id
            elif self.what == 'proj_file':
                obj = Projects.objects.get(slug__iexact=slug)
                form.instance.project_id = obj.id
            elif self.what == 'page_file':
                obj = ProjectPages.objects.get(slug__iexact=slug)
                form.instance.page_id = obj.id
            else:
                obj = None
            form.instance.user = self.request.user
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages, 'obj': obj, 'sub_page': sub_pages})




"""Класс для изменения объектов"""
class ObjectUpdateMixin:
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(instance=obj)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()
        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj, 'projects': projects, "pages": pages, 'sub_page': sub_pages})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(request.POST, instance=obj)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()

        if form.is_valid():
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj, 'projects': projects, "pages": pages, 'sub_page': sub_pages})


"""Класс для удаления объектов"""
class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'projects': projects, "pages": pages, 'sub_page': sub_pages})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))



class FileDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, pk):
        obj = self.model.objects.get(id=pk)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        sub_pages = ProjectPages.objects.all()
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'projects': projects, "pages": pages, 'sub_page': sub_pages})

    def post(self, request, pk):
        obj = self.model.objects.get(id=pk)
        obj.delete()
        return redirect(reverse(self.redirect_url))
