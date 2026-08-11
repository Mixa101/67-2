from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "image")
        widgets = {  # noqa: RUF012
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите заголовок"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите описание",
                }
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
