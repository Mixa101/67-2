from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from posts.models import Post

# Create your views here.


def hello_world(request: HttpRequest):
    return HttpResponse("<h1>Hello world!</h1>")


def post_list(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, "posts/posts.html", {"posts": posts})


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = Post.objects.get(id=id)

    return render(request, "posts/post_detail.html", {"post": post})
