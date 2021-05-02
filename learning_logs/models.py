from django.db import models
from django.utils import timezone


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    slug = models.SlugField(max_length=50, unique_for_date='date_added')
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    slug = models.SlugField(max_length=100, unique_for_date='date_added')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        postfix = ""
        if len(self.text) > 50:
            postfix = "..."
        return f"{self.text[:50]}{postfix}"
