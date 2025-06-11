from django import forms
from .models import Posts, Comments

class PostsModelForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = [""]

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["posts"]