from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import board_view, update_task_status, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', board_view, name='board'),  # главная — сразу доска
    path('task/<int:pk>/update/', update_task_status, name='update_task'),

    # API
    path('api/', include(router.urls)),
]
