from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'assignee', 'status', 'priority', 'order', 'created_at'
    )
    list_filter = ('status', 'priority', 'assignee')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority', 'order', 'assignee')
    ordering = ('status', 'order')
    list_per_page = 20

    readonly_fields = ('created_at', 'updated_at')
