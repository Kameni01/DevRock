from django.shortcuts import render, get_object_or_404, redirect
from .models import *




class ObjectDetailMixin:
    model = None
    template = None
    def get(self, request, id):
        obj = get_object_or_404(model, id=id)
        projects = Projects.objects.all()

        return render(request, self.template, {self.model.__name__.lower(): obj, "projects": projects})



class ShowObjectMixin:
    template = None
    exac_doc = None
    def get(self, request, id):
        cur_project = Projects.objects.get(id=id)
        projects = Projects.objects.all()
        if self.exac_doc == True:
            documents = ProjectPages.objects.filter(project_id=id)
            return render(request, self.template, context={"cur_project": cur_project, "documents": documents, 'projects' : projects})
        else:
            return render(request, self.template, context={"cur_project": cur_project, "projects" : projects})



class NonInheritedObjectCreateMixin:
    """Класс наследуемый для создания объектов ничего
    не наследующих от других объектов"""
    form_model = None
    template = None
    def get(self, request):
        form = self.form_model()
        projects = Projects.objects.all()
        return render(request, self.template, context={'form': form, "projects": projects})

    def post(self, request):
        form = self.form_model(request.POST, request.FILES)
        projects = Projects.objects.all()
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, "projects": projects})



class InheritedObjectCreateMixin:
    """Класс наследуемый для создания объектов наслудющих
    ключи других объектов автоматически"""
    form_model = None
    template = None
    def get(self, request, id):
        form = self.form_model()
        projects = Projects.objects.all()

        if self.what == 'proj':
            obj = get_object_or_404(Projects, id=id)
        elif self.what == 'page':
            obj = get_object_or_404(ProjectPages, id=id)
        elif self.what == 'proj_file':
            obj = get_object_or_404(ProjectFiles, id=id)
        elif self.what == 'page_file':
            obj = get_object_or_404(PageFiles, id=id)
        else:
            obj = None
        return render(request, self.template, context={'form': form, 'obj': obj, "projects": projects})

    def post(self, request, id):
        form = self.form_model(request.POST, request.FILES)
        if form.is_valid():
            if self.what == 'proj':
                obj = get_object_or_404(Projects, id=id)
                form.instance.project_id = obj.id
            elif self.what == 'page':
                obj = get_object_or_404(ProjectPages, id=id)
                form.instance.project_id = obj.project_id
                form.instance.parent_page = obj.id
            elif self.what == 'proj_file':
                obj = get_object_or_404(ProjectFiles, id=id)
                form.instance.project_id = obj.id
            elif self.what == 'page_file':
                obj = get_object_or_404(PageFiles, id=id)
                form.instance.page_id = obj.id
            else:
                obj = None
            form.instance.user = self.request.user
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, 'obj': obj})



class ObjectUpdateMixin:
    """Класс для изменения объектов"""
    model = None
    form_model = None
    template = None

    def get(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        form = self.form_model(instance=obj)
        projects = Projects.objects.all()

        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj, "projects": projects})

    def post(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        form = self.form_model(request.POST, instance=obj)
        projects = Projects.objects.all()

        if form.is_valid():
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj, "projects": projects})



class ObjectDeleteMixin:
    """Класс для удаления объектов"""
    model = None
    template = None
    redirect_url = None

    def get(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        projects = Projects.objects.all()

        return render(request, self.template, context={self.model.__name__.lower(): obj, "projects": projects})

    def post(self, request, id):
        obj = self.model.objects.get(id__iexact=id)
        obj.delete()

        return redirect(reverse(self.redirect_url))



class FileDeleteMixin:
    """Класс для удаления файлов со страниц и проектов"""
    model = None
    template = None
    redirect_url = None

    def get(self, request, id):
        obj = self.model.objects.get(id=id)
        projects = Projects.objects.all()

        return render(request, self.template, context={self.model.__name__.lower(): obj, "projects": projects})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        obj.delete()

        return redirect(reverse(self.redirect_url))
