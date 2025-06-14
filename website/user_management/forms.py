from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widget = {
            "email":forms.CharField(),
            "password":forms.PasswordInput(),
        }

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widget = {
            "password":forms.PasswordInput(),
        }

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widget = {
            "age":forms.IntegerField(min_value=15),
            "bio":forms.Textarea(),
        }