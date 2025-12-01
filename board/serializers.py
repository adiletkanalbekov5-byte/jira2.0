# =====================================================
#                   IMPORTS
# =====================================================
from rest_framework import serializers
from .models import Task


# =====================================================
#               Task Serializer (API)
# =====================================================
# Сериализатор превращает объект Task в JSON и обратно.
# ModelSerializer автоматически создаёт все поля на основе модели.
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task               # Модель, которую сериализуем
        fields = "__all__"         # Все поля модели будут в API

        # Если хочешь ограничить — можно указать:
        # fields = ["id", "title", "description", "status", "assignee"]
