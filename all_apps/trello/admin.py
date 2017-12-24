from django.contrib import admin

from .models import Board, Task, Tasklist

# Register your models here.

admin.site.register(Tasklist)
admin.site.register(Task)
admin.site.register(Board)