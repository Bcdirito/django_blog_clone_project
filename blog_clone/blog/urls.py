from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("about", views.AboutView.as_view(), name="about"),
    path("post/<slug:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("post/create", views.CreatePostView.as_view(), name="post_create"),
    path("post/<slug:pk>/update", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<slug:pk>/delete", views.PostDeleteView.as_view(), name="post_delete"),
    path("drafts", views.DraftListView.as_view(), name="drafts")
]