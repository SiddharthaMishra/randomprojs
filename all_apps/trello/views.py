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
    for index, taskID in enumerate(request.POST.getlist('item[]')):
        task = Task.objects.get(pk=taskID) 
        task.pos_in_list = index
        task.Tasklist = col
        task.save()
    return HttpResponse('done')

def add_task(request, board_no):
    board = get_object_or_404(Board, pk=board_no)
    col = board.tasklist_set.get(pk=int(request.POST['colID']))
    pos = col.task_set.all().count()
    text = request.POST['text']
    q = Task(Tasklist=col, task_text=text, pos_in_list = pos )
    q.save()
    return HttpResponse("<div class='task' id='item_"+str(q.id)+"'>"+text+"</div>")

def active(request, board_no):
    taskno = int(request.POST['pk'])
    q = Task.objects.get(pk=taskno)
    q.task_enabled = not q.task_enabled
    q.save()
    return HttpResponse("success")

def add_column(request, board_no):
    board = get_object_or_404(Board, pk=board_no)
    text = request.POST['text']
    q = Tasklist(Board=board, tasklist_name=text)
    q.save()
    return HttpResponse("<div class='column' id='col_"+str(q.id)+"'><h2 class='listName'>"+text+"</h2></div>")

def add_board(request):
    text = request.POST['text']
    q = Board(board_name=text)
    q.save()
    return HttpResponse("<li><a href="+str(q.id)+">"+text+"</a></li")