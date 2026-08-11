"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import UpdatePostView, create_post, hello_world, post_detail, post_list
from users.views import login_view, logout_view, register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello_world),
    path("posts/", post_list, name="post_list"),
    path("posts/<int:id>/", post_detail, name="post_detail"),
    path("posts/create/", create_post, name="post_create"),
    path("user/register/", register, name="register"),
    path("user/login/", login_view, name="login"),
    path("user/logout/", logout_view, name="logout"),
    path("posts/<int:pk>/update", UpdatePostView.as_view(), name="edit_post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
