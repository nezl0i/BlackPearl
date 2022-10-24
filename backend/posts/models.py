from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from users.models import User
from taggit.managers import TaggableManager
from transliterate import translit
import re


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(null=True, max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    header = models.CharField(max_length=250)
    # поле для человеко читаемой ссылки
    slug = models.SlugField(
        max_length=250,
        unique=True,
        blank=True,
        unique_for_date='publish'
    )
    # теги поста
    tags = TaggableManager()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    body = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def _create_unique_slug(self):
        magic = str(int(self.date_creation.timestamp()))
        return slugify(re.sub(r' +', '-', translit(self.header, language_code='ru', reversed=True))) + magic

    def save(self, *args, **kwargs):
        self.slug = self._create_unique_slug()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.header


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)
