from django.urls import path
from .views import get_tasks, create_task, update_task

urlpatterns = [
    path('', get_tasks),  # GET /api/tasks/
    path('create/', create_task),  # POST /api/tasks/create/
    path('update/<int:pk>/', update_task),  # PATCH /api/tasks/update/1/
]