from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponse
from .models import Task
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin



class ShowTasks(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all()
        comments = TaskComment.objects.all()
        return render(request, 'taskmanager/tasklist.html', context={"tasks":tasks, "user": request.user, 'comments': comments})


class ShowTask(LoginRequiredMixin, View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        tasks = Task.objects.all()
        comments = TaskComment.objects.filter(task=task)
        form = CommentForm()
        return render(request, 'taskmanager/task.html', context={"tasks":tasks, "form": form, 'comments': comments, "cur_task": task})


class TaskCreate(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all()
        form = TaskForm()
        return render(request, 'taskmanager/create_task.html', context={"form":form, "tasks": tasks})

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            task.author = request.user
            task.save()

        return redirect(reverse('taskmanager_url'))


class TaskDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()

        return redirect(reverse('taskmanager_url'))


class TaskEdit(LoginRequiredMixin, View):
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


class CommentAdd(LoginRequiredMixin, View):
    def get(self, request, id):
        tasks = Task.objects.all()
        comments = TaskComment.objects.all()
        form = CommentForm()
        return render(request, 'taskmanager/tasklist.html', context={"tasks":tasks, "comment_form":form, "current_form": id, "comments": comments})

    def post(self, request, id):
        form = CommentForm(request.POST)

        if form.is_valid():
            # comment = form.save()
            comment = TaskComment()
            comment.author = request.user
            comment.task = Task.objects.get(id=id)
            comment.body = form.cleaned_data["body"]

            comment.save()

        return redirect(reverse('task_url', kwargs={"id": id}))
