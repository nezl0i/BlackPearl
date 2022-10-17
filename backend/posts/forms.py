from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form for Post
    author and slug fields hidden 
    author fill in view
    slug changed when Post created
    """
    body = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('header', 'body', 'tags', 'id_category')