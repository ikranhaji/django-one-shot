from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem, TodoList
from .forms import TodoListForm


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


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail")
    else:
        form = TodoListForm
    context = {
        "form": form,
    }
    return render(request, 'todos/create.html', context)


def todo_list_update(request, id):
    list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=list)
        context = {
            "form": form,
        }
        return render(request, "todos/edit.html", context)
