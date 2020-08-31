from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

class OwnerView(LoginRequiredMixin, View):
	"""Hybrid View
	
	Extends:
		LoginRequiredMixin
		View
	"""

class OwnerListView(LoginRequiredMixin, ListView):
	"""Hybrid class
	
	Provides functionality of Login as well as ListView
	Extends:
		LoginRequiredMixin
		ListView
	"""

class OwnerDetailView(LoginRequiredMixin, DetailView):
	"""Hybrid DetailView

	Extends:
		LoginRequiredMixin
		DetailView
	"""

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
	"""Hybrid UpdateView
	
	Extends:
		LoginRequiredMixin
		UpdateView
	"""

class OwnerCreateView(LoginRequiredMixin, CreateView):
 	"""Hybrid CreateView
 	
 	Extends:
 		LoginRequiredMixin
 		CreateView
 	"""