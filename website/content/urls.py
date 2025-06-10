from django.urls import path
from .views import ContentCreateView, ContentFeedListView

urlpatterns = [
    path("",ContentFeedListView.as_view(),name="content_feed"),
    path("create/",ContentCreateView.as_view(),name="content_create")
]