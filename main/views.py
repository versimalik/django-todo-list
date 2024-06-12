from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Todo

# Create your views here.
def index(request):
    all_todos = Todo.objects.all()
    context = {
        'todos' : all_todos
    }
    return render(request, 'main/index.html', context)

def create(request):
    todo_text = request.POST['todo_text']
    todo_due_date = request.POST['todo_due_date']
    create_todo = Todo(text = todo_text, due_date = todo_due_date)
    create_todo.save()

    return HttpResponseRedirect(reverse('todo-index'))

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.status = not todo.status
    todo.save()

    return HttpResponseRedirect(reverse('todo-index'))

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return HttpResponseRedirect(reverse('todo-index'))
    