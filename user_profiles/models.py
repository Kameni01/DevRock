from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.text import slugify
from time import time
from django.urls import reverse



class TehnologyGroups(models.Model):
    group = models.CharField(max_length=25, verbose_name='Группа технологий')

    class Meta:
        verbose_name = "Группа технологий"
        verbose_name_plural = "Группы технологий"
        ordering = ["group"]

    def __str__(self):
        return self.title



class Tehnology(models.Model):
    group = models.ForeignKey(TehnologyGroups, verbose_name='Группа технологий', on_delete=models.CASCADE)
    tehno = models.CharField(verbose_name='Технология', max_length=25)

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"
        ordering = ["tehno"]

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя пользователя', blank=True, null=True, max_length=40)
    family = models.CharField(verbose_name='Фамилия пользователя', blank=True, null=True, max_length=40)
    stack = models.ManyToManyField(Tehnology, verbose_name='Стэк технологий')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    avatar = models.ImageField(upload_to='mezzanine/MainImg', height_field=None, width_field=None, max_length=256, blank=True, null=True)


    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["family", "name", "user"]

    def __str__(self):
        return self.title
