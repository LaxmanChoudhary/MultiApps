from django.urls import path
from home.views import HomeView, ProfileView

app_name='home'

urlpatterns = [
	path('', HomeView.as_view(), name="index"),
	path('profile/', ProfileView.as_view(), name='profile'),
]