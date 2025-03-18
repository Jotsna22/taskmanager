from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source="user.username"
    )  # Ensure user field is read-only

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "completed",
            "created_at",
            "updated_at",
            "user",
        ]
