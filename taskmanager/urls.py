from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:proj_id>', ShowTasks.as_view(), name="taskmanager_url"),
    path('<int:proj_id>/create/', TaskCreate.as_view(), name="create_task_url"),
    path('<int:proj_id>/<int:id>/delete/', TaskDelete.as_view(), name="delete_task_url"),
    path('<int:proj_id>/<int:id>/edit/', TaskEdit.as_view(), name="edit_task_url"),
    path('<int:proj_id>/<int:id>/comment', CommentAdd.as_view(), name="add_comment_url"),
    path('<int:proj_id>/<int:id>/', ShowTask.as_view(), name="task_url"),
    path('<int:proj_id>/<int:id>/status/<int:status>', TaskChangeStatus.as_view(), name='task_change_status')
]
