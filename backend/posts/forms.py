from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    """
    Form for Post
    author and slug fields hidden 
    author fill in view
    slug changed when Post created
    """
    body = forms.CharField(widget=SummernoteWidget(
        attrs={'summernote': {'width': '100%'}}), label='Содержание статьи')

    class Meta:
        model = Post
        fields = ('header', 'body', 'tags', 'id_category', 'image')
        labels = {
            'header': _('Заголовок'),
            'body': _('Содержание статьи'),
            'tags': _('Теги'),
            'id_category': _('Категория поста'),
            'image': _('Изображение')
        }
        error_messages = {
            'tags': {
                'max_length': _("Слишком длинное название"),
            },
            'tags': {
                'max_length': _("Слишком много тегов"),
            },
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
