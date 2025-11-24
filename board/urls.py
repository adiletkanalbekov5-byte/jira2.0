from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, board_view, update_task_status, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', index, name='index'),        # ← Главная страница
    path('board/', board_view, name='board'),
    path('task/<int:pk>/update/', update_task_status, name='update_task'),
    path('api/', include(router.urls)),      # API
]
