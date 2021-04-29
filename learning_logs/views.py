from django.shortcuts import render

def index(request):
    """Домашняя страница приложения learning_logs"""
    return render(request, 'learning_logs/index.html')
