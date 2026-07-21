from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


def hello_world(request: HttpRequest):
    return HttpResponse("<h1>Hello world!</h1>")
