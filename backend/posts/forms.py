from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
