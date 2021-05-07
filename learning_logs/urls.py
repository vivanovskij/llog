"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница для отображения тем
    path('topics/', views.topics, name='topics'),
    # Страница для отображения темы
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для создания новой темы 
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для создания записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
