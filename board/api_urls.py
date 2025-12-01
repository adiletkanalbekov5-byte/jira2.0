from rest_framework import routers
from .api import TaskViewSet  # Импортируем API-контроллер (ViewSet)

# -----------------------------
# Маршрутизатор DRF (создаёт URL для API)
# -----------------------------
router = routers.DefaultRouter()

# Регистрируем ViewSet:
# /api/tasks/        → список задач (GET), создание (POST)
# /api/tasks/<id>/   → получение, обновление, удаление (GET, PUT, PATCH, DELETE)
router.register(r'tasks', TaskViewSet, basename='task')

# DRF сам создаёт все нужные URL
urlpatterns = router.urls
