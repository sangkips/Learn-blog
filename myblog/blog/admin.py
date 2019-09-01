from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'published_date')
    list_filter = ('title',)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)

