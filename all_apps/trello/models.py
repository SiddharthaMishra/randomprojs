from django.db import models

# Create your models here.

class Board(models.Model):
    """ Model for the boards """
    board_name = models.CharField(max_length=20)
    def __str__(self):
        return self.board_name

class Tasklist(models.Model):
    """ Task Lists for each board """
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    tasklist_name = models.CharField(max_length=20)
    def __str__(self):
        return self.tasklist_name

class Task(models.Model):
    """Task for each list """
    Tasklist = models.ForeignKey(Tasklist, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=50)
    task_enabled = models.BooleanField(default=True)
    def __str__(self):
        return self.task_text