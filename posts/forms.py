from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "image")

    def clean_title(self) -> dict:
        title = self.cleaned_data["title"]

        if title == "banned word":
            raise forms.ValidationError("this word is banned")

        return self.cleaned_data
