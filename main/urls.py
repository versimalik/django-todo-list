from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="todo-index"),
    path('create/', views.create, name="todo-create"),
    path('update/<int:todo_id>', views.update, name="todo-update"),
    path('delete/<int:todo_id>', views.delete, name="todo-delete"),
]
