from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, upload_to="posts/")


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
