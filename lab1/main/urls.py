from django.urls import path
from main.views import task_incomplete_list,task_complete_list

urlpatterns = [
    path('todos/', task_incomplete_list),
    path('todos/<int:pk>/completed', task_complete_list)
]