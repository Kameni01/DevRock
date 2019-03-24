from django.shortcuts import render, get_object_or_404, redirect
from .models import *



class ShowObjectMixin:
    template = None
    use_model = None
    def get(self, request, id):
        data = get_object_or_404(use_model, id=id)

        return render(request, self.template, context={self.model.__name__.lower(): data})



class EditObjectMixin:
    template = None
    use_model = None
    form_model = None
    def get(self, request, id):
        data = get_object_or_404(use_model, id=id)
        form = self.form_model(instance=data)

        return render(request, self.template, context={'form': form, self.model.__name__.lower(): data})

    def post(self, request, id):
        data = get_object_or_404(use_model, id=id)
        form = self.form_model(instance=data)

        if form.is_valid():
            form.save()
            return redirect("{% url 'show_profile_url' id=id %}")
        else:
            return render(request, self.template, context={'form': form, self.model.__name__.lower(): data})
