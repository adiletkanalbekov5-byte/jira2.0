from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# -------------------------------------------------------
# Swagger / OpenAPI схема проекта
# -------------------------------------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="SimpleBoard API",        # Название API
        default_version='v1',           # Версия API
        description="API для SimpleBoard",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Swagger открыт для всех
)


urlpatterns = [
    # ---------------------------------------------------
    # Админка Django
    # ---------------------------------------------------
    path('admin/', admin.site.urls),

    # ---------------------------------------------------
    # Авторизация через Django Auth (HTML формы)
    # ---------------------------------------------------
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),

    # ---------------------------------------------------
    # JWT токены (логин для API)
    # ---------------------------------------------------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # получение токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # обновление токена

    # ---------------------------------------------------
    # API роуты приложения board (ViewSet + Router)
    # ---------------------------------------------------
    path('api/', include('board.api_urls')),  # берёт маршруты из board/api_urls.py

    # ---------------------------------------------------
    # Swagger документация
    # ---------------------------------------------------
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),

    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),

    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),

    # ---------------------------------------------------
    # Основной сайт (HTML страницы приложения board)
    # ---------------------------------------------------
    path('', include('board.urls')),
]
