from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .models import Profile
from .forms import ProfileModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

    
@login_required
def dashboard(request):
    if request.method == "POST":
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("dashboard")
    profile = Profile.objects.filter(user=request.user)
    if not profile:
        form = ProfileModelForm()
        return render(request, "user_management/dashboard.html", {"form":form})
    else:
        profile = Profile.objects.get(user=request.user)
        return render(request, "user_management/dashboard.html", context={"profile":profile})
        
    
    
    
