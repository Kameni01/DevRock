from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ShowTask.as_view(), name="taskmanager_url"),
    path('create/', TaskCreate.as_view(), name="create_task_url"),
    path('<int:id>/delete/', TaskDelete.as_view(), name="delete_task_url"),
    path('<int:id>/edit/', TaskEdit.as_view(), name="edit_task_url"),
    path('<int:id>/comment', CommentAdd.as_view(), name="add_comment_url")
]
