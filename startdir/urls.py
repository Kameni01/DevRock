from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

#from .views import

urlpatterns = [
    path('', TemplateView.as_view(template_name='startdir/homepage.html'), name="Home_Page"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
