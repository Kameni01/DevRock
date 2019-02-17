from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.http import HttpResponse
from .models import Task
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin

def render_my_tasks(request, proj_id):
    tasks = Task.objects.filter(author=request.user) \
            | Task.objects.filter(reviewer=request.user) | Task.objects.filter(executors__username__icontains=request.user)
    cur_project = Projects.objects.get(id=proj_id)
    projects = Projects.objects.all()
    return render(request, 'taskmanager/my_tasks.html',
                  context={"tasks": tasks, 'cur_project': cur_project,
                           'projects': projects})


class ShowTasks(LoginRequiredMixin, View):
    def get(self, request, proj_id):
        return render_my_tasks(request, proj_id)


class ShowTask(LoginRequiredMixin, View):
    def get(self, request, id, proj_id):
        task = Task.objects.get(id=id)
        tasks = Task.objects.filter(author=request.user)
        comments = TaskComment.objects.filter(task=task)
        cur_project = Projects.objects.get(id=proj_id)
        projects = Projects.objects.all()
        executors = task.executors.all()
        form = CommentForm()
        return render(
            request, 'taskmanager/task.html',
            context={"tasks":tasks, "form": form, 'comments': comments,
                     "cur_task": task, 'cur_project': cur_project,
                     'projects': projects, 'executors': executors})


class TaskCreate(LoginRequiredMixin, View):
    def get(self, request, proj_id):
        tasks = Task.objects.filter(author=request.user)
        cur_project = Projects.objects.get(id=proj_id)
        form = TaskForm()
        return render(request, 'taskmanager/create_task.html', context={"form":form, "tasks": tasks, 'cur_project': cur_project})

    def post(self, request, proj_id):
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            task.author = request.user
            task.save()

        return render_my_tasks(request, proj_id)


class TaskDelete(LoginRequiredMixin, View):
    def get(self, request, id, proj_id):
        task = Task.objects.get(id=id)
        task.delete()

        return render_my_tasks(request, proj_id)


class TaskEdit(LoginRequiredMixin, View):
    def get(self, request, id, proj_id):
        task = Task.objects.get(id=id)
        tasks = Task.objects.filter(author=request.user)
        cur_project = Projects.objects.get(id=proj_id)
        form = TaskForm(instance=task)

        return render(request, 'taskmanager/edit_task.html', context={"form":form, "task": task, "tasks":tasks, 'cur_project': cur_project})

    def post(self, request, id, proj_id):
        task = Task.objects.get(id=id)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()

        return redirect(
                reverse('task_url', kwargs={"id": id, 'proj_id': proj_id}))


class TaskChangeStatus(LoginRequiredMixin, View):
    def get(self, request, id, proj_id, status):
        task = Task.objects.get(id=id)
        task.status = status
        task.save()

        return render_my_tasks(request, proj_id)

    def post(self, request, id, proj_id, status):
        task = Task.objects.get(id=id)
        task.status = status
        task.save()

        return render_my_tasks(request, proj_id)



class CommentAdd(LoginRequiredMixin, View):
    def get(self, request, id, proj_id):
        return render_my_tasks(request, proj_id)
        # tasks = Task.objects.filter(author=request.user)
        # comments = TaskComment.objects.all()
        # cur_project = Projects.objects.get(id=proj_id)
        # form = CommentForm()

        # return render(request, 'taskmanager/tasklist.html', context={"tasks":tasks, "comment_form":form, "current_form": id, "comments": comments, 'cur_project': cur_project})

    def post(self, request, id, proj_id):
        form = CommentForm(request.POST)

        if form.is_valid():
            # comment = form.save()
            comment = TaskComment()
            comment.author = request.user
            comment.task = Task.objects.get(id=id)
            comment.body = form.cleaned_data["body"]

            comment.save()

        return redirect(reverse('task_url', kwargs={"id": id, 'proj_id': proj_id}))
