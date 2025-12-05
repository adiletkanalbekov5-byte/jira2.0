# =====================================================
#                     IMPORTS
# =====================================================
from django.urls import path, include
from rest_framework import routers

from .views import (
    board,
    add_task,
    move_task,
    task_detail,
    TaskViewSet,
    UserViewSet,
    TeamViewSet,
)

# =====================================================
#                    API ROUTER
# =====================================================
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register("users", UserViewSet)
router.register("teams", TeamViewSet)

# =====================================================
#                       URLS
# =====================================================

urlpatterns = [

    # HTML
    path('', board, name='board'),
    path('task/add/', add_task, name='add_task'),
    path('task/<int:id>/move/', move_task, name='move_task'),
    path('task/<int:id>/', task_detail, name='task_detail'),

    # API — теперь правильно
    path('api/', include(router.urls)),
]
