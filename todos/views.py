from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todos.models import Todo

# Create your views here.


def addTask(request):
    task = request.POST['task']
    Todo.objects.create(task = task)
    return redirect('home')

# def completedTask(request):
#     if request.method == "POST":
#         task_id = request.POST.get('task_id')
#         if task_id:
#             try:
#                 todo = Todo.objects.get(id=task_id)
#                 todo.task_completed = True
#                 todo.save()S
#             except Todo.DoesNotExist:
#                 pass
#     return redirect('home')
    
def completedTask(request, pk):
    task = get_object_or_404(Todo, pk = pk)
    task.task_completed = True
    task.save()
    print(task.task_completed)
    return redirect('home')
def UncompletedTask(request, pk):
    task = get_object_or_404(Todo, pk = pk)
    task.task_completed = False
    task.save()
    print(task.task_completed)
 
    return redirect('home')
def delete(request, pk):
    task = get_object_or_404(Todo, pk = pk)
    task.delete()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Todo, pk = pk)
    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()
        return redirect('home')
    else:
        context = {
            'task' : task
        }
    return render(request, 'edit_task.html', context)
   

  

