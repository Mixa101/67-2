from typing import Any

from django.db.models import Q
from django.forms.models import BaseModelForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from posts.forms import PostForm
from posts.models import Post, PostLikes

# Create your views here.


def hello_world(request: HttpRequest):
    return HttpResponse("<h1>Hello world!</h1>")


def post_list(request: HttpRequest):
    posts = Post.objects.select_related("user").order_by("-created_at")

    q = request.GET.get("q")

    if q:
        posts = posts.filter(Q(title__icontains=q) | Q(description__icontains=q))
    return render(request, "posts/posts.html", {"posts": posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id)
    return render(request, "posts/post_detail.html", {"post": post})


# def create_post(request: HttpRequest) -> HttpResponse:
#     if request.user.is_anonymous:
#         return redirect("login")
#     form = PostForm()
#     if request.method.lower() == "post":  # type: ignore
#         form = PostForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.instance.user = request.user
#             form.instance.save()
#             return redirect("post_list")

#     return render(request, "posts/create_post.html", context={"form": form})


class CreatePostView(CreateView):
    model = Post
    template_name = "posts/create_post.html"
    form_class = PostForm

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        if request.user.is_anonymous:
            return redirect("login")

        return super().post(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    form_class = PostForm


class MyPostsListView(ListView):
    model = Post
    template_name = "posts/my_posts.html"

    context_object_name = "posts"

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        if request.user.is_anonymous:
            return redirect("login")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user

        return context


class LikePostView(CreateView):
    model = PostLikes
    template_name = "posts/posts.html"
    fields = ("user",)
    success_url = reverse_lazy("post_list")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_anonymous:
            return redirect("login")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        post = get_object_or_404(Post, id=self.kwargs["pk"])
        form.instance.user = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        post = get_object_or_404(Post, id=self.kwargs["pk"])
        form.instance.user = self.request.user
        form.instance.post = post
        form.instance.save()
        return redirect("post_list")
