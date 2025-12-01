from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


# -------------------------------------------------------
# API для задач (CRUD)
# -------------------------------------------------------
# ModelViewSet автоматически создаёт:
#   GET    /api/tasks/        — список задач
#   POST   /api/tasks/        — создать задачу
#   GET    /api/tasks/<id>/   — получить одну задачу
#   PUT    /api/tasks/<id>/   — обновить задачу
#   PATCH  /api/tasks/<id>/   — частичное обновление
#   DELETE /api/tasks/<id>/   — удалить задачу
# -------------------------------------------------------
class TaskViewSet(viewsets.ModelViewSet):
    # Все задачи
    queryset = Task.objects.all()

    # Используем сериализатор TaskSerializer
    serializer_class = TaskSerializer

    # Запрещаем доступ неавторизованным пользователям (JWT/сессия)
    permission_classes = [IsAuthenticated]
