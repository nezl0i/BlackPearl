from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('header', 'body', 'tags', 'id_category')