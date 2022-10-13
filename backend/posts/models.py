from django.db import models
from django.utils import timezone
from users.models import User
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=20)

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
        unique_for_date='date_creation'
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

    def __str__(self):
        return self.header
