from django.shortcuts import render
from main.models import Task, Todo


def task_incomplete_list(request, pk):
    todo = Todo.objects.get(id=pk)
    tasks = Task.objects.filter(todo=todo, mark=False)
    context = {'tasks': tasks,
               'todo': todo,
               'number': pk
               }
    return render(request, 'todo_list.html', context=context)


def task_complete_list(request, pk):
    todo = Todo.objects.get(id=pk)
    tasks = Task.objects.filter(todo=todo, mark=True)
    context = {'tasks': tasks,
               'todo': todo,
               'number': pk
               }
    return render(request, 'todo_complete_list.html', context=context)
