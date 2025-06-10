from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Posts
from .forms import PostsModelForm
from django.urls import reverse_lazy

class ContentCreateView(CreateView):
    model = Posts
    form_class = PostsModelForm
    template_name = "content/content_creation.html"
    success_url = reverse_lazy("content_feed")

class ContentFeedListView(ListView):
    model = Posts
    template_name = "content/content_feed.html"
    context_object_name = "posts"