from django.contrib import admin

# Register your models here.
from task.models import TaskItem
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ["title" ,"created_at", "owner"]
    list_filter = ["done" , "owner"]
    search_fields = ["tite", "owner__email"]
admin.site.register(TaskItem, TaskModelAdmin)
