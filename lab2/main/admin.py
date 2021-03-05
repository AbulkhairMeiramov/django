from django.contrib import admin
from main.models import Todo, Task


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'due_on', 'owner', 'mark', 'todo']
    ordering = ['name']
    search_fields = ['name', 'todo__name', 'owner', 'mark']
    list_filter = ['created', 'due_on']
