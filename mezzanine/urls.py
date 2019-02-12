from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TreeRender.as_view(), name="mezzanine"),
    path('project/<int:id>/', ShowProject.as_view(), name='project_url'),
    path('project/create/', CreateProject.as_view(), name='createproject'),
    path('project/<int:id>/setting', ProjectDetail.as_view(), name='project_settings_url'),
    path('project/<int:id>/documents', ShowDocuments.as_view(), name='documents_url'),
    path('project/<int:id>/documents/add/', AddProjectFile.as_view(), name='add_rojectfile'),

    path('project/<int:pk>/delete', DeleteProjectFile.as_view(), name='delete_projectfile'),
    path('project/<str:slug>/', ProjectDetail.as_view(), name='projectdetail'),
    path('project/<str:slug>/update/', UpdateProject.as_view(), name='updateproject'),
    path('project/<str:slug>/delete/', ProjectDelete.as_view(), name='deleteproject'),
    path('project/<str:slug>/page/create/', CreatePage.as_view(), name='createpage'),
    path('projectpage/<str:slug>/addfile/', AddPageFile.as_view(), name='add_pagefile'),
    path('projectpage/<int:pk>/delete/', DeletePageFile.as_view(), name='delete_pagefile'),
    path('projectpage/<str:slug>/page/create/', CreatePageToPage.as_view(), name='pagetopage'),
    path('projectpage/<str:slug>/', PageDetail.as_view(), name='pagedetail'),
    path('projectpage/<str:slug>/update/', UpdatePage.as_view(), name='updatepage'),
    path('projectpage/<str:slug>/delete/', PageDelete.as_view(), name='deletepage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
