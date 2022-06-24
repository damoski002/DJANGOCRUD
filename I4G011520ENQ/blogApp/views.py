from pyexpat import model
from attr import fields
from django.views.generic.edit import Createview
from .models import Post

class blogAppCreateView(Createview):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class blogAppDetailview(Createview):
    model = Post

class blogAppUpdateview(Createview):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class blogAppDeleteview(Createview):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

