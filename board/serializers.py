# =====================================================
#                   IMPORTS
# =====================================================
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Team, Task
User = get_user_model()

# =====================================================
#               Task Serializer (API)
# =====================================================
# Сериализатор превращает объект Task в JSON и обратно.
# ModelSerializer автоматически создаёт все поля на основе модели.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class TeamSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task               # Модель, которую сериализуем
        fields = "__all__"         # Все поля модели будут в API

        # Если хочешь ограничить — можно указать:
        # fields = ["id", "title", "description", "status", "assignee"]
