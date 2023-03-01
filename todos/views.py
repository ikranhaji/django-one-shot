from django.shortcuts import render
from .models import TodoItem, TodoList


def todo_list_list(request):
    todolist = TodoList.objects.all()
    context = {
        "todolist_object": todolist
    }
    return render(request, "todos/list.html", context)
