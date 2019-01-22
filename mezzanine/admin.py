from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Projects, ProjectPages, ProjectFiles, PageFiles

admin.site.register(Projects)
admin.site.register(ProjectPages)
admin.site.register(ProjectFiles)
admin.site.register(PageFiles)
