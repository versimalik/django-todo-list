from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    user = request.user
    all_todos = Todo.objects.filter(user = user).order_by('-id')
    context = {
        'todos' : all_todos
    }
    return render(request, 'main/index.html', context)

def create(request):
    todo_text = request.POST['todo_text']
    todo_due_date = request.POST['todo_due_date']
    user = request.user
    create_todo = Todo(text = todo_text, due_date = todo_due_date, user = user)
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
    