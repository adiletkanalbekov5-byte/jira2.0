from django.contrib import admin
from .models import Task


# -------------------------------------------------------
# Настройка отображения модели Task в админ-панели Django
# -------------------------------------------------------
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    # Какие поля показывать в списке задач
    list_display = (
        'id',
        'title',
        'assignee',
        'status',
        'priority',
        'order',
        'created',
        'updated',
    )

    # Фильтры справа
    list_filter = ('status', 'priority', 'assignee')

    # Поля, по которым работает поиск
    search_fields = ('title', 'description')

    # Поля, которые можно редактировать прямо из списка (inline)
    list_editable = ('status', 'priority', 'order', 'assignee')

    # Сортировка по умолчанию
    ordering = ('status', 'order')

    # Кол-во задач на одной странице
    list_per_page = 20

    # Поля, которые нельзя редактировать вручную
    readonly_fields = ('created', 'updated')
