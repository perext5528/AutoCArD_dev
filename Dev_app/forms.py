from django import forms
from .models import Post


class Post_text(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
