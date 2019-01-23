from django.shortcuts import render, get_object_or_404, redirect
from .models import *



class ObjectCreateMixin:
    form_model = None
    template = None
    def get(self, request):
        form = self.form_model()
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()

        return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages})

    def post(self, request):
        form = self.form_model(request.POST, request.FILES)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()

        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, 'projects': projects, "pages": pages})



class ObjectUpdateMixin:
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(instance=obj)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj, 'projects': projects, "pages": pages})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(request.POST, instance=obj)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()

        if form.is_valid():
            form.save()
            return redirect("mezzanine")
        else:
            return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj, 'projects': projects, "pages": pages})



class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        projects = Projects.objects.all()
        pages = ProjectPages.objects.all()
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'projects': projects, "pages": pages})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
