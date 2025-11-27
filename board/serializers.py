from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    assignee_name = serializers.CharField(source="assignee.username", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "assignee", "assignee_name",
            "status", "priority", "order", "created_at", "updated_at"
        ]
        read_only_fields = ["created_at", "updated_at"]
