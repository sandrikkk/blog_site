from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["posts"]
        labels = {
            "user_name": "Your Name",
            "user_mail": "Your Email",
            "text": "Your Comment"
        }