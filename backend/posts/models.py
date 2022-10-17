from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from users.models import User
from taggit.managers import TaggableManager
from transliterate import translit
import re


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
        unique = True,
        blank = True
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

    def _create_unique_slug(self):
        magic = str(int(self.date_creation.timestamp()))
        return slugify(re.sub(r' +','-',translit(self.header, language_code='ru', reversed=True))) + magic

    def save(self, *args, **kwargs):
        self.slug = self._create_unique_slug()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.header
