from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # __lte -> less than or equal to
        # __ -> used for SQL calls
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")

class PostDetailView(DetailView):
    # same as show
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = "/login"
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login"
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("post_list")
    
    model = Post
    
class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/login"
    redirect_field_name = "blog/post_list.html"

    model = Post

    def get_queryset(self):
        # __isnull -> no publication date
        return Post.objects.filter(published_date__isnull=True).order_by("created_date")