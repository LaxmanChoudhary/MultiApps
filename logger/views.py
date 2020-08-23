from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from logger.models import Topic, Board
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import CreateForm

# Create your views here.
class LogListView(LoginRequiredMixin, ListView):
	model = Topic
	template_name = 'logger/log_main.html'
	success_url = reverse_lazy('logger:loglist')
	def get_queryset(self):
		qs = super(ListView, self).get_queryset()
		return qs.filter(creator=self.request.user)

class LogDetailView(LoginRequiredMixin, DetailView):
	model = Topic
	template_name = 'logger/log_detail.html'

class LogCreateView(LoginRequiredMixin, View):
	template_name = 'logger/log_form.html'
	success_url = reverse_lazy('logger:loglist')

	def get(self, request, pk=None):
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

class BoardListView(LoginRequiredMixin, ListView):
	model = Board
	template_name = 'logger/board_list.html'

class BoardDetailView(LoginRequiredMixin, View):
	template_name = 'logger/log_main.html'

	def get(self, request, pk):
		bd = get_object_or_404(Board, pk=pk)
		topics = get_list_or_404(Topic, boards=bd)
		ctx={'topic_list':topics}
		return render(request, self.template_name, ctx)
