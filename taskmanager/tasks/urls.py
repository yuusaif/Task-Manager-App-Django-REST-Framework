from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task_list_create'),
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task_retrieve_update_destroy'),
]
