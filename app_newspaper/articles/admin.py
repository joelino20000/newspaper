#articles/admin.py
from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    Extra =0

class ArticleAdmin (admin.ModelAdmin):
    inlines =[
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)