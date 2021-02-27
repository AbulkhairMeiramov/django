from django.shortcuts import render


def task_incomplete_list(request):
    tasks = [
        {
            'name': 'Task 1',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': False
        },
        {
            'name': 'Task 2',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': False
        },
        {
            'name': 'Task 3',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': False
        },
        {
            'name': 'Task 4',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': False
        }
    ]

    return render(request, 'todo_list.html', {'tasks': tasks})


def task_complete_list(request, pk):
    tasks = [
        {
            'name': 'Task 0',
            'created': '10/09/2018',
            'due_on': '12/09/2018',
            'owner': 'admin',
            'mark': True
        }
    ]

    return render(request, 'todo_complete_list.html', {'tasks': tasks, 'number': pk})

