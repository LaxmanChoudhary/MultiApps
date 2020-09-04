from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns =[
	path("", views.TodoMain.as_view(), name="todo_main"),
	path("task/create/", views.TaskCreate.as_view(), name="task_create"),
	path("task/<int:pk>", views.TaskDetail.as_view(), name="task_detail"),
	path("task/<int:pk>/complete", views.StatusComplete.as_view(), name="status_complete"),
	path("task/<int:pk>/incomplete", views.StatusIncomplete.as_view(), name="status_incomplete"),
	path("task/<int:pk>/delete", views.TaskDelete.as_view(), name="task_delete"),

	path("task-group/", views.GroupView.as_view(), name="group_view"),
	path("task-group/create", views.GroupCreate.as_view(), name="group_create"),
]