from django.urls import path
from logger.views import LogListView
app_name = 'logger'

urlpatterns=[
	path('', LogListView.as_view(), name='loglist'),
]