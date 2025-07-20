from django.contrib import admin

from todos.models import Todo

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'task_completed', 'updated_at')

admin.site.register(Todo,TaskAdmin)
