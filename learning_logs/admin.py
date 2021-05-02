from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug'  ,'text', 'date_added')
    list_filter = ('text',)
    prepopulated_fields = {'slug': ('text',)}
    ordering = ('-id',)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'date_added')
    list_filter = ('slug',)
    prepopulated_fields = {'slug': ('text',)}
    ordering = ('-id',)
