from django.urls import path
from .views import TaskListView, TaskCreateView, TaskRetrieveView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]