from django.urls import path
from .auth import SignUpPageView, LoginPageView, LogoutPageView
from . import auth
from .views import ProfileDetailView
from . import views

urlpatterns=[
    path("signup/", SignUpPageView.as_view(), name="signup"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("logout/", auth.logoutPage, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]