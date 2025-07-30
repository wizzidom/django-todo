from django.http import HttpResponse
from django.shortcuts import redirect

from todos.models import Todo

# Create your views here.


def addTask(request):
    task = request.POST['task']
    Todo.objects.create(task = task)
    return redirect('home')



