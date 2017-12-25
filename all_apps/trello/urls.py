""" URLs for Trello app """

from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('add_board/', views.add_board),
    path('<int:pk>/', views.BoardView.as_view(), name = 'board'),
    path('<int:board_no>/changePos/', views.change_pos),
    path('<int:board_no>/addTask/', views.add_task),
    path('<int:board_no>/active/', views.active),    
    path('<int:board_no>/add_col/', views.add_column),    
]