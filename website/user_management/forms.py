from django.contrib.auth.models import User
from django import forms

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