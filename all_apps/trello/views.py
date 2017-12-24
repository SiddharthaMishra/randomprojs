from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Board, Tasklist, Task
# Create your views here.

class IndexView(generic.ListView):
    model = Board
    template_name = 'trello/index.html'

class BoardView(generic.DetailView):
    model = Board
    template_name = 'trello/board.html'

