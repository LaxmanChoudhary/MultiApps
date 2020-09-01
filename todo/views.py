from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from home import owner
from todo.models import *
from todo.forms import *

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
	template_name = "todo/todo_form.html"
	success_url = reverse_lazy('todo:todo_main')

	def get(self, request, pk=None):
		tform = TaskForm(request.GET or None, users=request.user)
		ctx={'form':tform}
		return render(request, self.template_name, ctx)


	def post(self, request, pk=None):
		task = TaskForm(request.POST, users=request.user)
		frm = task.save(commit=False)
		frm.creator = request.user
		frm.save()
		return redirect(self.success_url)

class GroupView(owner.OwnerView):
	template_name = "todo/group_view.html"

	def get(self, request):
		t = Task.objects.all().order_by('task_group__name')
		ctx={'tasks':t}
		return render(request, self.template_name, ctx)
