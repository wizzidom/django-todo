from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length =250)
    task_completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 

    def __str__(self):
        return self.task