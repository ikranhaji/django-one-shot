from django.urls import path
from .views import (todo_list_list, todo_list_detail, todo_list_create,
                    todo_item_create,
                    todo_list_update, todo_list_delete)

urlpatterns = [
    path("todos/", todo_list_list, name="todo_list_list"),
    path("todos/<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("todos/create", todo_list_create, name="todo_list_create"),
    path("todos/<int:id>/edit", todo_list_update, name="todo_list_update"),
    path("todos/<int:id>/delete", todo_list_delete, name="todo_list_delete"),
    path("todos/items/create", todo_item_create, name="todo_item_create"),
]
