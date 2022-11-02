from django.contrib import admin
from .models import PostLikes


@admin.register(PostLikes)
class PostLikesAdmin(admin.ModelAdmin):
    list_display = ('post', 'liked_by', 'like', 'created')
    search_fields = ('liked_by', 'post')
