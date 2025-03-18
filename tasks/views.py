from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdminOrReadOnly
from .models import Task
from .serializer import TaskSerializer
from django.utils.dateparse import parse_date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .pagination import TaskPagination
from rest_framework.exceptions import ValidationError, NotFound
from django.shortcuts import get_object_or_404


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.select_related("user").all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["completed"]
    pagination_class = TaskPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        created_after = self.request.query_params.get("created_after")
        if created_after:
            date = parse_date(created_after)
            if date:
                queryset = queryset.filter(created_at__gte=date)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_object(self):
        task_id = self.kwargs.get("pk")
        task = get_object_or_404(Task, id=task_id)
        return task

    def perform_update(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise ValidationError({"error": str(e)})
