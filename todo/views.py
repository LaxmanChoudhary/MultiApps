from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View

from home import owner
from todo.models import *
from todo.forms import *

#main page
class TodoMain(owner.OwnerView):
	template_name = "todo/todo.html"

	def get(self, request):
#		taskgroup = TaskGroup.objects.filter(creator=request.user)
		gc = TaskGroup.objects.filter(creator=request.user).count()
		rt = Task.objects.filter(creator=request.user).filter(completed=False)[:5]
		ctx={'groups_count':gc, 'recent_tasks':rt}
		return render(request, self.template_name, ctx)

# model: task

class TaskListView(owner.OwnerView):
	template_name = "todo/task_list.html"

	def get(self, request):
		tasks = Task.objects.filter(creator=request.user)
		ctx={'tasks':tasks}
		return render(request, self.template_name, ctx)

class TaskDetail(owner.OwnerView):
	template_name= "todo/task_detail.html"

	def get(self, request, pk):
		task = Task.objects.get(id=pk)
		ctx ={'task':task}
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

class TaskDelete(owner.OwnerView):
	success_url = reverse_lazy('todo:todo_main')

	def post(self, request, pk):
		task = get_object_or_404(Task, id=pk)
		task.delete()
		try:
			return redirect(self.request.GET['next'])
		except:
			return redirect(self.success_url)

class StatusComplete(owner.OwnerView):
	success_url = reverse_lazy("todo:todo_main")
	def post(self, request, pk):
		task = get_object_or_404(Task, id=pk)
		task.completed = True
		task.save()
		try:
			return redirect(self.request.GET['next'])
		except:
			return redirect(self.success_url)

class StatusIncomplete(owner.OwnerView):
	success_url = reverse_lazy("todo:todo_main")
	def post(self, request, pk):
		task = get_object_or_404(Task, id=pk)
		task.completed = False
		task.save()
		try:
			return redirect(self.request.GET['next'])
		except:
			return redirect(self.success_url)

# model: TaskGroup
class GroupView(owner.OwnerView):
	template_name = "todo/group_view.html"

	def get(self, request):
		t = Task.objects.all().filter(creator=request.user).order_by('task_group__name')
		grps = TaskGroup.objects.filter(creator=request.user)
		form = GroupForm()
		ctx={'tasks':t, 'form':form, 'grps':grps}
		return render(request, self.template_name, ctx)

class GroupCreate(owner.OwnerView):
	success_url=reverse_lazy("todo:group_view")
	def post(self, request):
		grp = GroupForm(request.POST)
		group = grp.save(commit=False)
		group.creator = request.user
		group.save()
		try:
			return redirect(self.request.GET['next'])
		except:
			return redirect(self.success_url)

class GroupDeleteView(owner.OwnerView):
	success_url= reverse_lazy("todo:group_view")
	def post(self, request, pk):
		grp = get_object_or_404(TaskGroup, id=pk)
		grp.delete()
		try:
			return redirect(self.request.GET['next'])
		except:
			return redirect(self.success_url)
