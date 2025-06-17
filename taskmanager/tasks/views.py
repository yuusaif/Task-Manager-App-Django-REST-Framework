from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UserTaskBaseView(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

class TaskListView(UserTaskBaseView):
    pass

class TaskCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveView(UserTaskBaseView):
    pass

class TaskUpdateView(UserTaskBaseView, generics.UpdateAPIView):
    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.kwargs['pk'])

class TaskDeleteView(TaskUpdateView, generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"Message" : "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    