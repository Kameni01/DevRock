from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('<int:id>/', ShowProfile.as_view(), name='show_profile_url'),
    path('<int:id>/update/', EditProfile.as_view(), name='edit_profile_url')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
