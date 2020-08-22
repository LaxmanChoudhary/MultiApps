from django.shortcuts import render
from django.views.generic import ListView
from logger.models import Topic, Board
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

# Create your views here.
class LogListView(LoginRequiredMixin, ListView):
	model = Topic
	template_name = 'logger/log_main.html'
	success_url = reverse_lazy('logger:loglist')

class BoardListView(LoginRequiredMixin, ListView):
	model = Board
	template_name = 'logger/board_list.html'