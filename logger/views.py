from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View
from logger.models import Topic, Board
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import CreateForm

#Model: Topic
class LogListView(LoginRequiredMixin, View):
	model = Topic
	template_name = 'logger/log_main.html'
	#success_url = reverse_lazy('logger:log_list')
	'''
	def get_queryset(self):
		qs = super(ListView, self).get_queryset()
		return qs.filter(creator=self.request.user)
	'''
	def get(self, request):
		nex = request.path
		topic = Topic.objects.filter(creator=self.request.user)
		bc = Board.objects.filter(creator=self.request.user).count()
		ctx = {'topic_list':topic, 'bc':bc, 'next':nex}
		return render(request, self.template_name, ctx)

class LogDetailView(LoginRequiredMixin, DetailView):
	model = Topic
	template_name = 'logger/log_detail.html'

class LogCreateView(LoginRequiredMixin, View):
	template_name = 'logger/log_form.html'
	success_url = reverse_lazy('logger:log_list')

	def get(self, request, pk=None):
		#args to pass current user details to form
		#request.GET or None- makes sure no pre-errors are shown
		form = CreateForm(request.GET or None, user=request.user)
		ctx={'form':form}
		return render(request, self.template_name, ctx)

	def post(self, request, pk=None):
		form = CreateForm(request.POST, request.FILES or None, user=request.user)
		'''
		if not form.is_valid():
		ctx = {'form':form}
		return render(request, self.template_name, ctx)
		'''
		topic = Topic(date=request.POST['date'], name=request.POST['name'], 
			description=request.POST['description'], creator=request.user, 
			boards=Board.objects.get(pk=request.POST['boards']))
		topic.save()
		return redirect(self.success_url)

class LogUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'logger/log_form.html'
	success_url = reverse_lazy('logger:log_list')

	def get(self, request, pk):
		ob = get_object_or_404(Topic, id=pk, creator=self.request.user)
		form = CreateForm(instance=ob, user=request.user)
		ctx = {'form':form}
		return render(request, self.template_name, ctx)

	def post(self, request, pk=None):
		ob = get_object_or_404(Topic, id=pk, creator=self.request.user)
		form = CreateForm(request.POST, request.FILES or None, instance=ob, user=request.user)

		if not form.is_valid():
			ctx = {'form':form}
			return render(request, self.template_name, ctx)

		ob = form.save(commit=False)
		ob.save()

		return redirect(self.success_url)

class  LogDeleteView(LoginRequiredMixin, DeleteView):
	model = Topic
	template_name = 'logger/log_confirm_delete.html'
	success_url = reverse_lazy('logger:log_list')

	def get_queryset(self):
		qs= super(DeleteView, self).get_queryset()
		return qs.filter(creator=self.request.user)

#Model: Board
class BoardListView(LoginRequiredMixin, ListView):
	model = Board
	template_name = 'logger/board_list.html'

	def get_queryset(self):
		qs = super(ListView, self).get_queryset()
		return qs.filter(creator=self.request.user)

class BoardDetailView(LoginRequiredMixin, View):
	template_name = 'logger/log_main.html'

	def get(self, request, pk):
		bd = Board.objects.get(pk=pk)
		topics = Topic.objects.filter(boards=bd)
		ctx={'topic_list':topics}
		return render(request, self.template_name, ctx)

class BoardCreateView(LoginRequiredMixin, CreateView):
	model = Board
	fields = ['name']
	success_url = reverse_lazy('logger:board_list')

	#get_form() ref- https://docs.djangoproject.com/en/3.1/ref/class-based-views/mixins-editing/#formmixin
	def post(self, request, pk=None):
		form = super(CreateView, self).get_form()
		if not form.is_valid():
			ctx = {'form':form}
			return render(request, self.template_name, ctx)

		fm = form.save(commit=False)
		fm.creator = self.request.user
		fm.save()

		#either next passed by requesting page or board_list page
		try:
			return redirect(self.request.GET['next'])
		except:
			return redirect(self.success_url)

class BoardDeleteView(LoginRequiredMixin, DeleteView):
	model = Board
	template_name = "logger/board_confirm_delete.html"
	success_url = reverse_lazy('logger:board_list')

