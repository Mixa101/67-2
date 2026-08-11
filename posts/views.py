from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView

from posts.forms import PostForm
from posts.models import Post

# Create your views here.


def hello_world(request: HttpRequest):
    return HttpResponse("<h1>Hello world!</h1>")


def post_list(request: HttpRequest):
    posts = Post.objects.select_related("user").order_by("-created_at").all()

    return render(request, "posts/posts.html", {"posts": posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id)
    return render(request, "posts/post_detail.html", {"post": post})


def create_post(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return redirect("login")
    form = PostForm()
    if request.method.lower() == "post":  # type: ignore
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            form.instance.save()
            return redirect("post_list")

    return render(request, "posts/create_post.html", context={"form": form})


class UpdatePostView(UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    form_class = PostForm
