from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from home import owner
from todo.models import *

# Create your views here.
class TodoMain(owner.OwnerView):
	template_name = "todo/todo.html"

	def get(self, request):
#		taskgroup = TaskGroup.objects.filter(creator=request.user)
		gc = TaskGroup.objects.filter(creator=request.user).count()
		rt = Task.objects.all()[:5]
		ctx={'groups_count':gc, 'recent_tasks':rt}
		return render(request, self.template_name, ctx)

class TaskCreate(owner.OwnerView):
	success_url = reverse_lazy('todo:todo_main')

	def get(self, request):
		""

	def post(self, request, pk=None):
		task = Task(title = request.POST['name'], text=request.POST['text'] , task_group=TaskGroup.objects.get(pk=request.POST['task_group']), creator=request.user)
		task.save()
		return redirect(self.success_url)

class GroupView(owner.OwnerView):
	template_name = "todo/group_view.html"

	def get(self, request):
		t = Task.objects.all().order_by('task_group__name')
		ctx={'tasks':t}
		return render(request, self.template_name, ctx)
