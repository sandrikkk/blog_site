from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.views import View

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        quary_set = super().get_queryset()
        data = quary_set[:3]
        return data
    

class PostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

    
class PostDetailsViews(View):
    template_name = "blog/post-detail.html"
    model = Post

    def get(self, request, slug):
        post = Post.objects.get(slug = slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "cooment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug = slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.posts  = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args = [slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "cooment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)