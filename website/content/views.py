from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Posts, Comments
from .forms import PostsModelForm, CommentModelForm
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

class CommentCreateView(CreateView):
    model = Comments
    form_class = CommentModelForm
    template_name = "content/comment.html"
    success_url = reverse_lazy("content_feed")

    def form_valid(self, form, **kwargs):
        instance = form.save(commit=False)
        pk = self.kwargs.get("pk")
        instance.posts = Posts.objects.get(id = pk)
        form = instance
        form.save()
        return redirect("content_feed")