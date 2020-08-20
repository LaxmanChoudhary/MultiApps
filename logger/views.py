from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class LogListView(TemplateView):
	template_name = 'logger/log_main.html'