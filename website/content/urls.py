from django.urls import path
from .views import ContentCreateView, ContentFeedListView, CommentCreateView

urlpatterns = [
    path("", ContentFeedListView.as_view(), name="content_feed"),
    path("create/", ContentCreateView.as_view(), name="content_create"),
    path("comment/<int:pk>/", CommentCreateView.as_view(), name="comment"),
]