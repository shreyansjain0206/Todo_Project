from django.urls import path
from . import views

urlpatterns = [
    path("tasks", views.task_page),
    path("tasks/update/<int:task_id>", views.update_task_page),
     path("tasks/delete/<int:task_id>", views.delete_task_page),
    path("add-task", views.add_task_page),

    path("api/tasks", views.get_tasks),

    path("api/tasks/create", views.create_task),

    path("api/tasks/update/<int:task_id>", views.update_task),

    path("api/tasks/delete/<int:task_id>", views.delete_task),

]