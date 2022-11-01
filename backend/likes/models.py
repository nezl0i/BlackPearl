from django.db import models
from django.utils import timezone
from posts.models import Post
from users.models import User


class PostLikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, verbose_name='Статья')
    liked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Поставил лайк')
    like = models.BooleanField('Like', default=False)
    created = models.DateTimeField('Created', default=timezone.now)

    def __str__(self):
        return f'{self.liked_by}: {self.post} {self.like}'

    class Meta:
        verbose_name = 'Post like'
        verbose_name_plural = 'Post likes'
