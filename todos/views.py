from django.shortcuts import render, get_object_or_404
from .models import TodoItem, TodoList


def todo_list_list(request):
    todolists = TodoList.objects.all()
    context = {
        "todolist_object": todolists
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_detail": todolist
    }
    return render(request, "todos/detail.html", context)
