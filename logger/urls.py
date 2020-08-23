from django.urls import path
from logger.views import *

app_name = 'logger'

urlpatterns = [
    #model- Topic
    path('', LogListView.as_view(), name='loglist'),
    path('log/<int:pk>/', LogDetailView.as_view(), name='logdetail'),
    path('log/create/', LogCreateView.as_view(), name='logcreate'),

    #model- Board
    path('boards/', BoardListView.as_view(), name='boardlist'),
    path('board/<int:pk>/', BoardDetailView.as_view(), name='boarddetail'),
]
