from django.db import models
from django.contrib.auth.models import User
from mezzanine.models import Projects


class Task(models.Model):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    REVIEW = 3
    STATUSES = ((TODO, 'To do',), (IN_PROGRESS, 'In progress',),
                (DONE, 'Done',), (REVIEW, 'On review',) )

    title = models.CharField(max_length=160, db_index=True)
    body = models.TextField(blank=True)
    status = models.IntegerField(default=TODO, choices=STATUSES)
    project = models.ForeignKey(Projects, null=True, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True)

    author = models.ForeignKey(User, verbose_name='Автор', related_name="Task_author", on_delete=models.SET_NULL, null=True)
    reviewer = models.ForeignKey(User, verbose_name='Проверяющий', related_name="Task_reviewer", on_delete=models.SET_NULL, null=True)
    executors = models.ManyToManyField(User, verbose_name='Исполнители')

    def __str__(self):
        return self.title


class TaskComment(models.Model):
    body = models.TextField()
    task = models.ForeignKey(Task, verbose_name="Комментарий", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, related_name="TaskComment_author", null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body