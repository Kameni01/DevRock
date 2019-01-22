from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import TreeRender, ProjectDetail, PageDetail

urlpatterns = [
    path('', TreeRender, name="mezzanine"),
    path('project/<str:slug>', ProjectDetail, name='projectdetail'),
    path('prohectpage/<str:slug>', PageDetail, name='pagedetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
