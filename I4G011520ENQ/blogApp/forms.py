from socket import fromshare
from attr import fields
from django import froms
from matplotlib.pyplot import title
from .models import Post
class PostForm(forms.Form):
    class meta:
        model = Post
        fields = [
            "title",
            "description"
        ]