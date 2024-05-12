from django.contrib import admin
from .models import Story, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Story)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title',)
    search_fields = ['title']
    summernote_fields = ('story_text',)


admin.site.register(Comment)
