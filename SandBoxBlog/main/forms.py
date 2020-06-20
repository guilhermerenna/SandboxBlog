from django import forms
from .models import Post

class Post(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    author = forms.CharField(label="Title", max_length=200)
    content = forms.CharField(label="Title", max_length=2000)