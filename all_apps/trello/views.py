from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import generic

from .models import Board, Tasklist, Task
# Create your views here.

class IndexView(generic.ListView):
    model = Board
    template_name = 'trello/index.html'

class BoardView(generic.DetailView):
    model = Board
    template_name = 'trello/board.html'

def change_pos(request, board_no):
    board = get_object_or_404(Board, pk=board_no)
    col = board.tasklist_set.get(pk=int(request.POST['colID'][4:]))
    print(col.pk)
    print(request.POST.get('item[]'))

    for index, taskID in enumerate(request.POST.get('item[]')):
      #  print(index)
        task = Task.objects.get(pk=taskID) 
        task.pos_in_list = index
        task.Tasklist = col
        task.save()

    return HttpResponse('done')


