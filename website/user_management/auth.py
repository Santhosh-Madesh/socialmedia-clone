from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import SignUpModelForm, LoginModelForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

class SignUpPageView(CreateView):
    model = User
    form_class = SignUpModelForm
    template_name = "user_management/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)

class LoginPageView(LoginView):
    redirect_authenticated_user = True
    template_name = "user_management/login.html"
    success_url = reverse_lazy("content_feed")
    
class LogoutPageView(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")
    
def logoutPage(request):
    logout(request)
    return redirect("login")