from django.contrib import admin
from .models import Author, Post


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'name')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)