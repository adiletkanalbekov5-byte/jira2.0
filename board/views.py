# -----------------------------------------------
# Импорты Django
# -----------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

# -----------------------------------------------
# Импорты DRF (API)
# -----------------------------------------------
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# -----------------------------------------------
# Внутренние импорты
# -----------------------------------------------
from .models import Task
from .serializers import TaskSerializer


# =====================================================
#               API (DRF ViewSet)
# =====================================================

class TaskViewSet(viewsets.ModelViewSet):
    """
    API для модели Task.
    Позволяет выполнять полный CRUD:
    - GET /api/tasks/
    - POST /api/tasks/
    - PUT/PATCH /api/tasks/<id>/
    - DELETE /api/tasks/<id>/
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # AllowAny — чтобы Swagger работал без авторизации
    permission_classes = [AllowAny]


# =====================================================
#               HTML Views (Сайт)
# =====================================================

@login_required
def board(request):
    """
    Главная страница: Канбан-доска.
    Возвращает 3 колонки с задачами:
    - todo
    - progress
    - done
    """
    return render(request, 'board.html', {
        'user': request.user,
        'todo': Task.objects.filter(status='todo'),
        'progress': Task.objects.filter(status='progress'),
        'done': Task.objects.filter(status='done'),
        'users': User.objects.all(),
    })


@login_required
def add_task(request):
    """
    Создание новой задачи из формы board.html.
    Выполняется только POST-запрос.
    """
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        assignee_id = request.POST.get('assignee')
        assignee = User.objects.get(id=assignee_id) if assignee_id else None

        Task.objects.create(
            title=title,
            description=description,
            assignee=assignee
        )

    return redirect('board')


@login_required
def update_task_status(request, pk):
    """
    Обновление статуса задачи (например, при drag & drop).
    Возвращает partial HTML (фрагмент задачи).
    """
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        new_status = request.POST.get('status')

        # Проверка корректности статуса
        if new_status in ['todo', 'progress', 'done']:
            task.status = new_status
            task.order = Task.objects.filter(status=new_status).count()
            task.save()

            # Генерация фрагмента HTML
            html = render_to_string("partials/task.html", {"task": task})
            return HttpResponse("OK")

    return HttpResponse("Ошибка", status=400)


# =====================================================
#        Перемещение задач через JS (AJAX)
# =====================================================

@csrf_exempt  # drag & drop из JS без CSRF
@login_required
def move_task(request, id):
    """
    Перемещение задачи между колонками через AJAX.
    Используется в реальном drag & drop на странице.
    """
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        new_status = request.POST.get('status')

        if new_status in ['todo', 'progress', 'done']:
            task.status = new_status
            task.save()
            return JsonResponse({'success': True})

    return JsonResponse({'error': 'Invalid request'}, status=400)


# =====================================================
#        Детальная страница задачи
# =====================================================

@login_required
def task_detail(request, id):
    """
    Отдельная HTML-страница задачи.
    Показывает:
    - название
    - описание
    - исполнитель
    - статус
    """
    task = get_object_or_404(Task, id=id)
    return render(request, 'task_detail.html', {'task': task})
