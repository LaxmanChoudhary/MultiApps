from django.urls import path
from logger.views import LogListView, BoardListView

app_name = 'logger'

urlpatterns=[
	path('', LogListView.as_view(), name='loglist'),
	path('boards/', BoardListView.as_view(), name='boardlist'),
]