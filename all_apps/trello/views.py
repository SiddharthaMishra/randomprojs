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
    """ To update the new positions of the tasks in the database """
    
    board = get_object_or_404(Board, pk=board_no)
    col = board.tasklist_set.get(pk=int(request.POST['colID']))

    for index, taskID in enumerate(request.POST.getlist('item[]')):
        task = Task.objects.get(pk=taskID) 
        task.pos_in_list = index    # positions updated according to their index in the sent array
        task.Tasklist = col     # in case tasks change column
        task.save()

    return HttpResponse('')


def add_task(request, board_no):
    """ To add new task """

    board = get_object_or_404(Board, pk=board_no)
    col = board.tasklist_set.get(pk=int(request.POST['colID']))
    pos = col.task_set.all().count()    # pos_in_list of the new task 
    text = request.POST['text']
    q = Task(Tasklist=col, task_text=text, pos_in_list = pos )
    q.save()
    return HttpResponse("<div class='task' id='item_" + str(q.id) + "'>" + text + "</div>") # Returns object to be rendered

def active(request, board_no):
    """ Inverts the active state to the task """

    taskno = int(request.POST['pk'])
    q = Task.objects.get(pk=taskno)
    q.task_enabled = not q.task_enabled
    q.save()
    return HttpResponse("")

def add_column(request, board_no):
    """ Adds new tasklist """

    board = get_object_or_404(Board, pk=board_no)
    text = request.POST['text']
    q = Tasklist(Board=board, tasklist_name=text)
    q.save()
    return HttpResponse("<div class='column' id='col_"+str(q.id)+"'><h2 class='listName'>"+text+"</h2></div>")

def add_board(request):
    """ Adds new Board """
    text = request.POST['text']
    q = Board(board_name=text)
    q.save()
    return HttpResponse("<li><a href="+str(q.id)+">"+text+"</a></li")