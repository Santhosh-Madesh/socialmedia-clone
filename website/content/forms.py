from django import forms
from .models import Posts

class PostsModelForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = [""]