from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class Projects(models.Model):
    """Класс проектов"""
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    mainimg = models.ImageField(upload_to='mezzanine/MainImg', height_field=None, width_field=None, max_length=100, null=True)
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    slug = models.SlugField(verbose_name='slug' ,max_length=150, unique=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title



class ProjectPages(models.Model):
    """Класс страниц проектов"""
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, verbose_name='Проект', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField(verbose_name='slug' ,max_length=150, unique=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title



class ProjectFiles(models.Model):
    """Класс файлов"""
    user = models.ForeignKey(User, verbose_name='Загрузил', on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, verbose_name='Проект', on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name="Имя файла", null=True, max_length=100)
    file = models.FileField(upload_to='files/', verbose_name='Файл', null=True)

    class Meta:
        verbose_name = "Файл проекта"
        verbose_name_plural = 'Файлы проекта'

    def __str__(self):
        return self.title



class PageFiles(models.Model):
    """Класс файлов"""
    user = models.ForeignKey(User, verbose_name='Загрузил', on_delete=models.CASCADE)
    page = models.ForeignKey(ProjectPages, verbose_name='Страница', on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name="Имя файла", null=True, max_length=100)
    file = models.FileField(upload_to='files/', verbose_name='Файл', null=True)

    class Meta:
        verbose_name = "Файл страницы"
        verbose_name_plural = 'Файлы страницы'

    def __str__(self):
        return self.title
