from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, TeamViewSet, UserViewSet
# -----------------------------
# Маршрутизатор DRF (создаёт URL для API)
# -----------------------------
router = routers.DefaultRouter()

# Регистрируем ViewSet:
# /api/tasks/        → список задач (GET), создание (POST)
# /api/tasks/<id>/   → получение, обновление, удаление (GET, PUT, PATCH, DELETE)
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
# DRF сам создаёт все нужные URL
urlpatterns = router.urls
