from django.urls import path
from main.views import task_incomplete_list,task_complete_list

urlpatterns = [
    path('', task_incomplete_list),
    path('<int:pk>/completed', task_complete_list)
]