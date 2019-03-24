from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *



class ShowProfile(LoginRequiredMixin, ShowObjectMixin, View):
    template = 'show_profile_template.html'
    use_model = Profile
    raise_exception = True

class EditProfile(LoginRequiredMixin, EditObjectMixin, View):
    template = 'edit_profile_template.html'
    use_model = Profile
    form_model = EditProfileForm
    raise_exception = True
