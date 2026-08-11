from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField()


class Tag(models.Model):
    name = models.CharField()


class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, upload_to="posts/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.pk})


class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.post.pk})


# # Create your models here.
# # C-R-U-D

# # Create
# # SQL -> "INSERT INTO table_name (fields_name ...) VALUES (a, a, a);"
# # Django
# Post.objects.create()
# post = Post(title="title#1", description="description to blog")
# post.save()

# # Read
# # SQL -> "SELECT * FROM table_name WHERE title="title";"
# # Django
# post = Post.objects.filter(title="title").first()

# # Update
# # SQL -> "UPDATE table_name SET field_name=title WHERE title=title;"
# # Django
# post.title = "kasd asfas fasf"  # type: ignore
# post.save()  # type: ignore

# # Delete
# # SQL -> "DELETE FROM table_name WHERE title=title;"
# # Django
# post.delete()  # type: ignore
