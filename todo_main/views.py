
from django.shortcuts import render
from todos.models import Todo


def home(request): 
    tasks = Todo.objects.filter(task_completed = False).order_by('-updated_at')
    print(tasks)
    context = {
        'tasks' : tasks
    }
    return render(request, 'home.html', context)