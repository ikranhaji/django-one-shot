from django.urls import path
from .views import todo_list_list, todo_list_detail, todo_list_create, todo_list_update

urlpatterns = [
    path("todos/", todo_list_list, name="todo_list_list"),
    path("todos/<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("todos/create", todo_list_create, name="todo_list_create"),
    path("todos/<int:id>/edit", todo_list_update, name="todo_list_update"),
]
