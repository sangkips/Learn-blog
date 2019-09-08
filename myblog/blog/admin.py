from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'published_date')
    list_filter = ('title',)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

