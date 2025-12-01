# =====================================================
#                     IMPORTS
# =====================================================
from django.urls import path, include
from rest_framework import routers

# Views (HTML + API)
from .views import (
    board,
    add_task,
    move_task,
    task_detail,
    TaskViewSet
)


# =====================================================
#                    API ROUTER
# =====================================================
# Создаём DRF Router для автоматической генерации:
# /api/tasks/  (GET, POST)
# /api/tasks/<id>/ (GET, PUT, PATCH, DELETE)
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')


# =====================================================
#                       URLS
# =====================================================

urlpatterns = [

    # -------------------------------
    #        HTML маршруты
    # -------------------------------
    path('', board, name='board'),                         # Главная — Канбан доска
    path('task/add/', add_task, name='add_task'),          # Создание задачи
    path('task/<int:id>/move/', move_task, name='move_task'),  # Перемещение задачи
    path('task/<int:id>/', task_detail, name='task_detail'),   # Детальная страница задачи

    # -------------------------------
    #        API маршруты (DRF)
    # -------------------------------
    path('api/', include(router.urls)),   # Подключаем все /api/tasks/
]
