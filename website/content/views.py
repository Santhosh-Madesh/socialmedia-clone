from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Posts, Comments
from .forms import PostsModelForm, CommentModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name="dispatch")
class ContentCreateView(CreateView):
    model = Posts
    form_class = PostsModelForm
    template_name = "content/content_creation.html"
    success_url = reverse_lazy("content_feed")

@method_decorator(login_required, name="dispatch")
class ContentFeedListView(ListView):
    model = Posts
    template_name = "content/content_feed.html"
    context_object_name = "posts"

@method_decorator(login_required, name="dispatch")
class CommentCreateView(CreateView):
    model = Comments
    form_class = CommentModelForm
    template_name = "content/comment.html"
    success_url = reverse_lazy("content_feed")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        context["comments"] = Comments.objects.filter(posts=pk)
        return context

    def form_valid(self, form, **kwargs):
        instance = form.save(commit=False)
        pk = self.kwargs.get("pk")
        instance.posts = Posts.objects.get(id = pk)
        form = instance
        form.save()
        return redirect("content_feed")

def like(request, pk):
    post = Posts.objects.get(id = pk)
    post.likes += 1
    post.save()
    return redirect("content_feed")