from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponse
from .models import Task
from .forms import *

# Create your views here.
def show_task(request):
    tasks = Task.objects.all()
    print(request.user)
    return render(request, 'taskmanager/tasklist.html', context={"tasks":tasks, "user": request.user})


class TaskCreate(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'taskmanager/create_task.html', context={"form":form})

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            task.creator = request.user
            task.save()

        return redirect(reverse('taskmanager_url'))


class TaskDelete(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()

        return redirect(reverse('taskmanager_url'))


class TaskEdit(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        form = TaskForm(instance=task)

        return render(request, 'taskmanager/edit_task.html', context={"form":form, "task": task})

    def post(self, request, id):
        task = Task.objects.get(id=id)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()

        return redirect(reverse('taskmanager_url'))