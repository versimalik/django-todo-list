from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

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

    context = {'todo': create_todo}
    html_message = render_to_string('main/email/todo_added.html', context)

    send_mail(
        subject="[no-reply]New Todo Added",
        message=strip_tags(html_message),
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
        html_message=html_message,
        fail_silently=False
    )

    return HttpResponseRedirect(reverse('todo-index'))

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.status = not todo.status
    todo.save()

    todo_status_message = None
    if todo.status:
        todo_status_message = "Done"
    else:
        todo_status_message = "Not Done"

    message = "New Todo is updated!\n"  
    message += f"{todo.text} is set to {todo_status_message}\n"
    message += f"Due date: {todo.due_date}"

    send_mail(
        subject="[no-reply]New Todo Updated!",
        message=message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
        fail_silently=False
    )

    return HttpResponseRedirect(reverse('todo-index'))

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    message = "Todo is deleted!\n"  
    message += f"{todo.text} is deleted\n"
    message += f"Due date: {todo.due_date}"

    send_mail(
        subject="[no-reply]New Todo Deleted!",
        message=message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
        fail_silently=False
    )

    return HttpResponseRedirect(reverse('todo-index'))
    