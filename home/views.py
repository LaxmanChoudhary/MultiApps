from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(View):
	def get(self, request):
			return render(request, 'home/index.html')

class ProfileView(LoginRequiredMixin, View):
	def get(self, request):
		user = request.user
		ctx={'user':user}
		return render(request, 'home/profile.html', ctx)