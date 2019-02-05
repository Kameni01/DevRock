from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from mezzanine.models import Projects
from .utils import get_all_projects_enumerated




class Task(models.Model):
    TODO = 0
    INPROGRESS = 1
    REVIEW = 2
    DONE = 3
    STATUSES = ((TODO, 'ToDo',), (INPROGRESS, 'InProgress',),
                    (REVIEW, 'Review',), (DONE, 'Done',))

    DEFAULT_PROJECT = "Нет"

    title = models.CharField(max_length=160, db_index=True)
    body = models.TextField(blank=True)
    status = models.IntegerField(default=TODO, choices=STATUSES)
    project = models.TextField(choices=get_all_projects_enumerated(), null=True, default=DEFAULT_PROJECT)

    creation_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, null=True)
    # reviewer = profile
    # comments

    def __str__(self):
        return self.title
