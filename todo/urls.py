from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns =[
	path("", views.TodoMain.as_view(), name="todo_main"),
	path("task/create/", views.TaskCreate.as_view(), name="task_create"),

	path("task-group/", views.GroupView.as_view(), name="group_view"),
]