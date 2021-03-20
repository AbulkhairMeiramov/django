from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Todo(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    due_on = models.DateField()
    owner = models.CharField(max_length=255)
    mark = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

