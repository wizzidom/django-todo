
from django.shortcuts import render
from todos.models import Todo


def home(request): 
    tasks = Todo.objects.filter(task_completed = False).order_by('-updated_at')
    completed = Todo.objects.filter(task_completed = True)
    print(tasks)
    print(completed)
    context = {
        'tasks' : tasks,
        'completed' : completed
    }
    return render(request, 'home.html', context)


