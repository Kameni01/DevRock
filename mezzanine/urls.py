from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TreeRender, name="mezzanine"),
    path('project/create/', CreateProject.as_view(), name='createproject'),
    path('project/addfile/', AddProjectFile.as_view(), name='add_rojectfile'),
    path('project/<int:pk>/delete', DeleteProjectFile.as_view(), name='delete_projectfile'),
    path('project/<str:slug>/', ProjectDetail, name='projectdetail'),
    path('project/<str:slug>/update/', update_project.as_view(), name='updateproject'),
    path('project/<str:slug>/delete/', ProjectDelete.as_view(), name='deleteproject'),
    path('projectpage/create/', CreatePage.as_view(), name='createpage'),
    path('projectpage/addfile/', AddPageFile.as_view(), name='add_pagefile'),
    path('projectpage/<int:pk>/delete/', DeletePageFile.as_view(), name='delete_pagefile'),
    path('projectpage/<str:slug>/', PageDetail, name='pagedetail'),
    path('projectpage/<str:slug>/update/', update_page.as_view(), name='updatepage'),
    path('projectpage/<str:slug>/delete/', PageDelete.as_view(), name='deletepage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
