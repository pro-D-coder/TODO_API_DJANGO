from django.urls import path
from .views import ListTodo, DetailTodo, CreateTodo

urlpatterns = [
    path('create/', CreateTodo.as_view()),
    path('<slug:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
]
