from django.contrib import admin
from posts.models import Post, Category
from users.models import User, BanList, BanStatus
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(BanList)
admin.site.register(BanStatus)
