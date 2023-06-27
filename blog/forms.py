from django import forms
from .models import BlogPost, Tag, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['user']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
