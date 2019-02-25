from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# def Tree():
#     """Функция для создания переменных хранящих данные
#     для построения древа проектов(Была инкапсулированна
#     для уменьшения объема кода)"""
#     projects = Projects.objects.all()
#     pages = ProjectPages.objects.all()
#     sub_pages = ProjectPages.objects.all()
#
#     return projects, pages, sub_pages



class ShowObjectMixin:
    template = None
    exac_doc = None
    def get(self, request, id):
        cur_project = Projects.objects.get(id=id)
        projects = Projects.objects.all()
        if exac_doc == True:
            documents = ProjectPages.objects.filter(project_id=id)

        return render(request, self.template, context={"cur_project": cur_project, "documents": documents, 'projects' : projects})



class NonInheritedObjectCreateMixin:
    """Класс наследуемый для создания объектов ничего
    не наследующих от других объектов"""
    form_model = None
    template = None
    def get(self, request):
        form = self.form_model()
        # projects, pages, sub_pages = Tree()

        # return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages, 'sub_page': sub_pages})
        return render(request, self.template, context={'form': form})

    def post(self, request):
        form = self.form_model(request.POST, request.FILES)
        # projects, pages, sub_pages = Tree()

        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            return redirect("mezzanine")
        else:
            # return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages, 'sub_page': sub_pages})
            return render(request, self.template, context={'form': form})



class InheritedObjectCreateMixin:
    """Класс наследуемый для создания объектов наслудющих
    ключи других объектов автоматически"""
    form_model = None
    template = None
    def get(self, request, slug):
        form = self.form_model()
        # projects, pages, sub_pages = Tree()
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
        # return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages, 'obj': obj, 'sub_page': sub_pages})
        return render(request, self.template, context={'form': form, 'obj': obj})

    def post(self, request, slug):
        form = self.form_model(request.POST, request.FILES)
        # projects, pages, sub_pages = Tree()

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
            # return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages, 'obj': obj, 'sub_page': sub_pages})
            return render(request, self.template, context={'form': form, 'obj': obj})



class ObjectUpdateMixin:
    """Класс для изменения объектов"""
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(instance=obj)
        # projects, pages, sub_pages = Tree()

        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(request.POST, instance=obj)
        # projects, pages, sub_pages = Tree()


        if form.is_valid():
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj})



class ObjectDeleteMixin:
    """Класс для удаления объектов"""
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        # projects, pages, sub_pages = Tree()

        # return render(request, self.template, context={self.model.__name__.lower(): obj, 'projects': projects, "pages": pages, 'sub_page': sub_pages})
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()

        return redirect(reverse(self.redirect_url))



class FileDeleteMixin:
    """Класс для удаления файлов со страниц и проектов"""
    model = None
    template = None
    redirect_url = None

    def get(self, request, pk):
        obj = self.model.objects.get(id=pk)
        # projects, pages, sub_pages = Tree()

        # return render(request, self.template, context={self.model.__name__.lower(): obj, 'projects': projects, "pages": pages, 'sub_page': sub_pages})
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, pk):
        obj = self.model.objects.get(id=pk)
        obj.delete()

        return redirect(reverse(self.redirect_url))
