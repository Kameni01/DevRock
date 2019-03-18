from django.db import models
from django.contrib.auth.models import User
from mezzanine.models import Projects


class Task(models.Model):
    """Модель для создания заданий в таскменеджере"""
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    REVIEW = 3
    STATUSES = ((TODO, 'To do',), (IN_PROGRESS, 'In progress',),
                (DONE, 'Done',), (REVIEW, 'On review',) )

    title = models.CharField(verbose_name='Заголовок', max_length=160, null=True, blank=True, db_index=True)
    body = models.TextField(verbose_name='Тело задания', blank=True, null=True)
    status = models.IntegerField(verbose_name='Статус', default=TODO, choices=STATUSES)
    project = models.ForeignKey(Projects, verbose_name='Связано с проектом', blank=True, null=True, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    deadline_date = models.DateTimeField(verbose_name='Дата дедлайна',  blank=True, null=True)

    author = models.ForeignKey(User, verbose_name='Автор', related_name="Task_author", on_delete=models.SET_NULL, null=True)
    reviewer = models.ForeignKey(User, verbose_name='Проверяющий', related_name="Task_reviewer", on_delete=models.SET_NULL, null=True)
    executors = models.ManyToManyField(User, verbose_name='Исполнители')

    def __str__(self):
        return self.title


class TaskComment(models.Model):
    body = models.TextField(verbose_name='Текст комментария', null=True, blank=True)
    task = models.ForeignKey(Task, verbose_name="Комментарий", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, related_name="TaskComment_author", null=True)
    creation_date = models.DateTimeField(verbose_name='Дата создания комментария', auto_now_add=True)

    def __str__(self):
        return self.body
