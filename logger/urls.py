from django.urls import path
from logger.views import *

app_name = 'logger'

urlpatterns = [
    #model- Topic
    path('', LogListView.as_view(), name='log_list'),
    path('log/<int:pk>', LogDetailView.as_view(), name='log_detail'),
    path('log/create', LogCreateView.as_view(), name='log_create'),
    path('log/<int:pk>/delete', LogDeleteView.as_view(), name='log_delete'),
    path('log/<int:pk>/update', LogUpdateView.as_view(), name='log_update'),

    #model- Board
    path('boards', BoardListView.as_view(), name='board_list'),
    path('board/<int:pk>', BoardDetailView.as_view(), name='board_detail'),
    path('board/create', BoardCreateView.as_view(), name='board_create'),
    path('board/<int:pk>/delete', BoardDeleteView.as_view(), name='board_delete'),
]
