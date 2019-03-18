from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.text import slugify
from time import time
from django.urls import reverse


# def gen_slug(s):
#     new_slug = slugify(s, allow_unicode=True)
#     return new_slug + '-' +str(int(time()))


class Projects(models.Model):
    """Класс проектов"""
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    mainimg = models.ImageField(upload_to='mezzanine/MainImg', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    slug = models.SlugField(verbose_name='slug', blank=True, null=True, max_length=150, unique=True)
    ended = models.BooleanField(verbose_name='Готовность', blank=True, null=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse('projectdetail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('updateproject', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('deleteproject', kwargs={'id': self.id})

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     if self.created:
    #         pass
    #     super().save(*args, **kwargs)


    def __str__(self):
        return self.title

class DevComand(models.Model):
    project = models.ForeignKey(Projects, verbose_name='Проект', on_delete=models.CASCADE)
    developers = models.ManyToManyField(User, verbose_name='Разработчик')



class ProjectPages(models.Model):
    """Класс страниц проектов"""
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, verbose_name='Проект', null=True, blank=True, on_delete=models.CASCADE)
    parent_page = models.IntegerField(verbose_name='Родительская страница', null=True, blank=True)
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    # slug = models.SlugField(verbose_name='slug' , blank=True, null=True, max_length=150, unique=True)
    # level = models.IntegerField(verbose_name='Уровень наследования', null=True, blank=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ["title"]


    def get_absolute_url(self):
        return reverse('pagedetail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('updatepage', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('deletepage', kwargs={'id': self.id})

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     if self.created:
    #         pass
    #     super().save(*args, **kwargs)


    def __str__(self):
        return self.title



class ProjectFiles(models.Model):
    """Класс файлов проекта"""
    user = models.ForeignKey(User, verbose_name='Загрузил', on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, verbose_name='Проект', on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name="Имя файла", blank=True, null=True, max_length=100)
    file = models.FileField(upload_to='files/', verbose_name='Файл', null=True)

    class Meta:
        verbose_name = "Файл проекта"
        verbose_name_plural = 'Файлы проекта'

    def __str__(self):
        return self.title



class PageFiles(models.Model):
    """Класс файлов страницы"""
    user = models.ForeignKey(User, verbose_name='Загрузил', on_delete=models.CASCADE)
    page = models.ForeignKey(ProjectPages, verbose_name='Страница', on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name="Имя файла", blank=True, null=True, max_length=100)
    file = models.FileField(upload_to='files/', verbose_name='Файл', null=True)

    class Meta:
        verbose_name = "Файл страницы"
        verbose_name_plural = 'Файлы страницы'

    def __str__(self):
        return self.title
